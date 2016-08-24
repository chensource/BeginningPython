import re
import time
import json
import logging
import hashlib
import base64
import asyncio

from coroweb import get, post

from models import User, Comment, Blog, next_id


@get('/')
def index(request):
    logging.info('test User.findAll()')
    users = User.findAll()
    return {'__template__': 'test.html', 'users': users}
