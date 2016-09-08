import aiomysql
import asyncio


import random

codeSeedA = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def digit(raw):
    l = len(raw)
    # randrange() 是关于生产平均分配值更复杂 . int(random()*n) 这可能会产生轻微的不均匀分布。
    return raw[random.randrange(l)]


def codeGen(n):
    codes_pool = []
    for i in range(n):
        code = ""
        for i in range(10):
            code += digit(codeSeedA)
        codes_pool.append(code)
    return codes_pool

async def create_pool(loop, **kw):
    # logging.info('create database connection pool...')

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


async def execute(sql, args, autocommit=True):
    # log(sql, args)
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

async def select(sql, args, size=None):
    # log(sql, args)
    async with __pool.get() as conn:
        # 等待连接对象返回DictCursor可以通过dict的方式获取数据库对象，需要通过游标对象执行SQL
        async with conn.cursor(aiomysql.DictCursor) as cur:
            await cur.execute(
                sql,
                args)  #将sql中的'?'替换为'%s'，因为mysql语句中的占位符为%s
            #如果传入size'
            if size:
                resultset = await cur.fetchmany(size)  # 从数据库获取指定的行数
            else:
                resultset = await cur.fetchall()  # 返回所有的结果集
        # logging.info('rows returned: %s' % len(resultset))
        return resultset

class Model():
    async def save(self):
        # args = list(map(self.getValueOrDefault, self.__fields__))
        # args.append(self.getValueOrDefault(self.__primary_key__))
        # logging.info(args)
        codes = codeGen(200)
        for i in codes:
            await execute("insert into codes value ('%s')" % str(i) ,None)

    @classmethod
    async def findAll(cls, where=None, args=None, **kw):
        rs = await select('select * from codes', None)
        return [cls(**r) for r in rs]

async def test(loop):
    await create_pool(loop=loop,
                               user='sa',
                               password='P@ssw0rd',
                               db='awesome')
    a = Model()
    # await a.save()
    users = await a.findAll()

    for i in users:
        print('code:%s' % i)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test(loop))
    loop.close()
