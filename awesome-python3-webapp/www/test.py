import orm
import asyncio
import sys
from models import User, Blog, Comment


@asyncio.coroutine
def test(loop):
    yield from orm.create_pool(loop=loop,
                               user='sa',
                               password='P@ssw0rd',
                               db='awesome')
    u = User(name='chenshi2',
             email='280580216@qq.com',
             passwd='123456',
             image='about:blank')
    yield from u.save()


loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()
if loop.is_closed():
    sys.exit(0)
