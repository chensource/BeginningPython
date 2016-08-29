import orm
import asyncio
import sys
from models import User, Blog, Comment
import logging
import hashlib
# from confi_default import configs



# async def test(loop):
#     await orm.create_pool(loop=loop,
#                                user='sa',
#                                password='P@ssw0rd',
#                                db='awesome')
#     u = User(name='chenshi',
#              email='280580217@qq.com',
#              passwd='123456',
#              image='about:blank')
#     await u.save()
#     users = User.find('0147201758559317d4ca7b200aa46caa9967cce9ae86107000')
    # logging.info(users)
    # users = yield from User.findAll()
    # for x in users:
    #     logging.info('name is %s , passwd is %s' % (x.name, x.passwd))


sha1 = hashlib.sha1()
sha1.update('123456@qq.com'.encode('utf-8'))
print(sha1.hexdigest())

sha1.update(b':')
print(sha1.hexdigest())

sha1.update('123456'.encode('utf-8'))
print(sha1.hexdigest())

# loop = asyncio.get_event_loop()
# loop.run_until_complete(test(loop))
# loop.close()
# if loop.is_closed():
#     sys.exit(0)


