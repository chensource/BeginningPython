import re, time, json, logging, hashlib, base64, asyncio

from coroweb import get, post

from models import User, Comment, Blog, next_id

# @get('/')
# async def index(request):
#     logging.info('users')
#     users = await User.findAll()
#     return {'__template__': 'test.html', 'users': users}
#
#
# @get('/test')
# async def index(request):
#     logging.info('test')
#     users = await User.findAll()
#     return {'__template__': 'test.html', 'users': users}


# 测试
@get('/')
async def index(request):
    users = await User.findAll()
    return {'__template__': 'test.html', 'users': users}
