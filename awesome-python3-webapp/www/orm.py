import logging
import asyncio
import os
import json
import time
import aiomysql
from datetime import datetime
from aiohttp import websocket
logging.basicConfig(level=logging.INFO)


async def create_pool(loop, **kw):
    logging.info('create database connection pool...')

    global __pool
    __pool = await aiomysql.create_pool(host=kw.get('host', 'localhost'),
                                        port=kw.get('port', 3306),
                                        user=kw['user'],
                                        password=kw['password'],
                                        db=kw['db'],
                                        charset=kw.get('charset', 'utf8'),
                                        autocommit=kw.get('autocommit', True),
                                        maxsize=kw.get('maxsize', 10),
                                        minsize=kw.get('minsize', 1),
                                        loop=loop)


def log(sql, args=()):
    logging.info('SQL: %s' % sql)


async def select(sql, args, size=None):
    log(sql, args)
    async with __pool.get() as conn:
        # 等待连接对象返回DictCursor可以通过dict的方式获取数据库对象，需要通过游标对象执行SQL
        async with conn.cursor(aiomysql.DictCursor) as cur:
            await cur.execute(
                sql.replace('?', '%s'),
                args)  #将sql中的'?'替换为'%s'，因为mysql语句中的占位符为%s
            #如果传入size'
            if size:
                resultset = await cur.fetchmany(size)  # 从数据库获取指定的行数
            else:
                resultset = await cur.fetchall()  # 返回所有的结果集
        logging.info('rows returned: %s' % len(resultset))
        return resultset


async def execute(sql, args, autocommit=True):
    log(sql, args)
    async with __pool.get() as conn:
        if not autocommit:  # 若数据库的事务为非自动提交的,则调用协程启动连接
            await conn.begin()
        try:
            async with conn.cursor(
                aiomysql.
                DictCursor) as cur:  # 打开一个DictCursor,它与普通游标的不同在于,以dict形式返回结果
                await cur.execute(sql.replace('?', '%s'), args)
                affected = cur.rowcount  # 返回受影响的行数
            if not autocommit:  # 同上, 事务非自动提交型的,手动调用协程提交增删改事务
                await conn.commit()
        except BaseException as e:
            if not autocommit:  # 出错, 回滚事务到增删改之前
                await conn.rollback()
            raise e
        return affected


def create_args_string(num):
    L = []
    for n in range(num):
        L.append('?')
    return ', '.join(L)


class Field(object):
    def __init__(self, name, column_type, primary_key, default):
        self.name = name
        self.column_type = column_type
        self.primary_key = primary_key
        self.default = default

    def __str__(self):
        return '<%s,%s:%s>' % (self.__class__.__name__, self.column_type,
                               self.name)


class StringField(Field):
    def __init__(self,
                 name=None,
                 primary_key=False,
                 default=None,
                 ddl='varchar(100)'):
        super().__init__(name, ddl, primary_key, default)


class BooleanField(Field):
    def __init__(self, name=None, default=False):
        super().__init__(name, 'boolean', False, default)


class IntegerField(Field):
    def __init__(self, name=None, primary_key=False, default=0):
        super().__init__(name, 'bigint', primary_key, default)


class FloatField(Field):
    def __init__(self, name=None, primary_key=False, default=0.0):
        super().__init__(name, 'real', primary_key, default)


class TextField(Field):
    def __init__(self, name=None, default=None):
        super().__init__(name, 'text', False, default)


class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)

        #获取Table 的名称
        tableName = attrs.get('__table__', None) or name
        logging.info(' found model:%s (table:%s)' % (name, tableName))

        mappings = dict()
        fields = []
        primaryKey = None
        for k, v in attrs.items():
            if isinstance(v, Field):
                logging.info(' found mapping :%s ==> %s' % (k, v))
                mappings[k] = v
                if v.primary_key:
                    if primaryKey:
                        raise StandardError(
                            'Duplicate primary key for field: %s' % k)
                    primaryKey = k
                else:
                    fields.append(k)
        if not primaryKey:
            raise RuntimeError('primary key not found.')
        for k in mappings.keys():
            attrs.pop(k)
        escaped_fields = list(map(lambda f: '%s' % f, fields))
        attrs['__mappings__'] = mappings  # 属性和列之间的映射关系
        attrs['__table__'] = tableName  #表名
        attrs['__primary_key__'] = primaryKey  # 主键属性名
        attrs['__fields__'] = fields  #除开主键以外的名

        attrs['__select__'] = 'select `%s`, %s from `%s`' % (
            primaryKey, ', '.join(escaped_fields), tableName)
        attrs['__insert__'] = 'insert into `%s` (%s, `%s`) values (%s)' % (
            tableName, ', '.join(escaped_fields), primaryKey,
            create_args_string(len(escaped_fields) + 1))
        attrs['__update__'] = 'update `%s` set %s where `%s`=?' % (
            tableName, ', '.join(map(
                lambda f: '`%s`=?' % (mappings.get(f).name or f), fields)),
            primaryKey)
        attrs['__delete__'] = 'delete from `%s` where `%s`=?' % (tableName,
                                                                 primaryKey)
        return type.__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def getValue(self, key):
        return getattr(self, key, None)

    def getValueOrDefault(self, key):
        value = getattr(self, key, None)
        if value is None:
            field = self.__mappings__[key]
            logging.info("key:%s, default value:%s" % (key, field.default))
            if field.default is not None:
                value = field.default() if callable(
                    field.default) else field.default
                logging.debug('using default value for %s: %s' %
                              (key, str(value)))
                setattr(self, key, value)
        return value

    @classmethod
    async def find(cls, pk):
        logging.info('find object by primary key')
        rs = await select('%s where `%s`=?' %
                          (cls.__select__, cls.__primary_key__), [pk], 1)
        if len(rs) == 0:
            return None
        return cls(**rs[0])

    async def save(self):
        args = list(map(self.getValueOrDefault, self.__fields__))
        args.append(self.getValueOrDefault(self.__primary_key__))
        logging.info(args)
        rows = await execute(self.__insert__, args)
        if rows != 1:
            logging.warn('failed to insert record: affected rows: %s' % rows)

    @classmethod
    async def findAll(cls, where=None, args=None, **kw):
        ' find objects by where clause. '
        sql = [cls.__select__]
        # logging.info(cls.__select__)
        logging.info(select(' '.join(sql), args))
        if where:
            sql.append('where')
            sql.append(where)
        if args is None:
            args = []
        orderby = kw.get('orderby', None)
        if orderby:
            sql.append('order by ')
            sql.append(orderby)
        limit = kw.get('limit', None)
        if limit is not None:
            sql.append('limit')
            if isinstance(limit, int):
                sql.append('?')
                args.append(limit)
            elif isinstance(limit, tuple) and len(limit) == 2:
                sql.append('?')
                args.extend(limit)
            else:
                raise ValueError('Invalid limit value: %s' % str(limit))
        rs = await select(' '.join(sql), args)
        return [cls(**r) for r in rs]
