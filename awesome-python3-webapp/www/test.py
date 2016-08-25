import orm
import asyncio
import sys
from models import User, Blog, Comment
import logging
# from confi_default import configs


@asyncio.coroutine
def test(loop):
    yield from orm.create_pool(loop=loop,
                               user='sa',
                               password='P@ssw0rd',
                               db='awesome')
    # u = User(name='chenshi2',
    #          email='280580216@qq.com',
    #          passwd='123456',
    #          image='about:blank')
    # yield from u.save()
    # users = User.find('0147201758559317d4ca7b200aa46caa9967cce9ae86107000')
    # logging.info(users)
    users = yield from User.findAll()
    for x in users:
      logging.info('name is %s , passwd is %s' % (x.name,x.passwd))


loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
