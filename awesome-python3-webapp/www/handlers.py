import re
import time
import json
import logging
import hashlib
import base64
import asyncio

from coroweb import get, post
from apis import APIValueError, APIResourceNotFoundError, APIError, APIPermissionError
from models import User, Comment, Blog, next_id
from aiohttp import web
from config import configs

import markdown2

_RE_EMAIL = re.compile(
    r'^[a-z0-9\.\-\_]+\@[a-z0-9\-\_]+(\.[a-z0-9\-\_]+){1,4}$')
_RE_SHA1 = re.compile(r'^[0-9a-f]{40}$')
COOKIE_NAME = 'awesession'
_COOKIE_KEY = configs.session.secret


def check_admin(request):
    if request.__user__ is None or not request.__user__.admin:
        raise APIPermissionError("user is not admin")


def get_page_index(page_str):
    p = 1
    try:
        p = int(page_str)
    except Exception as e:
        pass
    if p < 1:
        p = 1
    return p


def text2html(text):
    lines = map(
        lambda s: '<p>%s</p>' % s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;'),
        filter(lambda s: s.strip() != '', text.split('\n')))
    return ''.join(lines)


def user2cookie(user, max_age):
    expires = str(int(time.time() + max_age))
    s = '%s-%s-%s-%s' % (user.id, user.passwd, expires, _COOKIE_KEY)
    L = [user.id, expires, hashlib.sha1(s.encode('utf-8')).hexdigest()]
    return '-'.join(L)


async def cookie2user(cookie_str):
    if not cookie_str:
        return None
    try:
        L = cookie_str.split('-')
        if len(L) != 3:
            return None
        uid, expires, sha1 = L
        if int(expires) < time.time():
            return None
        user = await User.find(uid)
        if user is None:
            return None
        s = '%s-%s-%s-%s' % (user.id, user.passwd, expires, _COOKIE_KEY)
        if sha1 != hashlib.sha1(s.encode('utf-8')).hexdigest():
            logging.info('invalid sha1')
            return None
        user.passwd = '******'
        return user
    except Exception as e:
        logging.exception(e)
        return None


@post('/api/authenticate')
async def authenticate(*, email, passwd):
    if not email:
        raise APIValueError('Email', 'Invalid email')
    if not passwd:
        raise APIValueError('Password', 'Invalid password')

    users = await User.findAll('email=?', [email])
    if len(users) == 0:
        raise APIValueError('email', 'Email not exist')

    user = users[0]
    # logging.info('user.passwd : %s , user.email: %s' % (user.passwd,user.email))
    # sha1 = hashlib.sha1()

    # sha1.update(user.email.encode('utf-8'))
    # sha1.update(b':')
    # sha1.update(passwd.encode('utf-8'))
    if user.passwd != passwd:
        raise APIValueError('password', 'Invalid password')

    r = web.Response()
    r.set_cookie(COOKIE_NAME,
                 user2cookie(user, 86400),
                 max_age=86400,
                 httponly=True)
    user.passwd = '******'
    r.content_type = 'application/json'
    # 序列化用户信息
    r.body = json.dumps(user, ensure_ascii=False).encode('utf-8')
    return r


@get('/')
def index(request):
    summary = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
    blogs = [
        Blog(id='1',
             name='Test Blog',
             summary=summary,
             created_at=time.time() - 120),
        Blog(id='2',
             name='Something New',
             summary=summary,
             created_at=time.time() - 3600),
        Blog(id='3',
             name='Learn Swift',
             summary=summary,
             created_at=time.time() - 7200),
        Blog(id='4',
             name='Learn Swift',
             summary=summary,
             created_at=time.time() - 14400),
        Blog(id='5',
             name='Learning Python',
             summary=summary,
             created_at=time.time() - 14400)
    ]
    return {'__template__': 'blogs.html', 'blogs': blogs}


@get('/blog/{id}')
async def get_blog(id):
    blog = await Blog.find(id)
    comments = await Comment.findAll('blog_id=?', [id], orderBy='created_at')
    for c in comments:
        c.html_content = text2html(c.content)
    blog.html_content = markdown2.markdown(blog.content)
    return {'__template__': 'blog.html', 'blog': blog, 'comments': comments}


@get('/manage/blogs/create')
def manage_create_blog():
    return {
        '__template__': 'manage_blog_edit.html',
        'id': '',
        'action': '/api/blogs'
    }


@get('/register')
def register():
    return {'__template__': 'register.html'}


@get('/signin')
def signig():
    return {'__template__': 'signin.html'}


@get('/api/users')
async def api_get_users():
    users = await User.findAll(orderBy='created_at desc')
    for u in users:
        u.passwd = '******'
    return dict(users=users)


@post('/api/users')
async def api_register_user(*, email, name, passwd):
    if not name or not name.strip():
        raise APIValueError('name')
    if not email or not _RE_EMAIL.match(email):
        raise APIValueError('email')
    if not passwd or not _RE_SHA1.match(passwd):
        raise APIValueError('password')

    users = await User.findAll('email=?', [email])
    if len(users) > 0:
        raise APIError('register failed', 'email', 'Email is already in use')

    uid = next_id()
    # sha1_passwd = '%s:%s' % (uid, passwd)
    logging.info(passwd)
    passwd = passwd
    image = 'http://www.gravatar.com/avatar/%s?d=mm&s=120' % hashlib.md5(
        email.encode('utf-8')).hexdigest()
    user = User(uid=uid,
                name=name.strip(),
                email=email,
                passwd=passwd,
                image=image)
    await user.save()
    # make session in cookie
    r = web.Response()
    r.set_cookie(COOKIE_NAME,
                 user2cookie(user, 86400),
                 max_age=86400,
                 httponly=True)
    user.passwd = '********'
    r.content_type = 'application/json'
    r.body = json.dumps(user, ensure_ascii=False).encode('utf-8')
    return r


@get('/api/blogs/{id}')
async def api_get_blog(*, id):
    blog = await Blog.find(id)
    return blog


@post('/api/blogs')
async def api_create_blog(request, *, name, summary, content):
    check_admin(request)
    if not name or name.strip():
        raise APIValueError('name', 'name cannot be empty')
    if not summary or summary.strip():
        raise APIValueError('summary', 'summary cannot be empty')
    if not content or content.strip():
        raise APIValueError('content', 'content cannot be empty')
    user = request.__user__
    blog = Blog(user_id=user.id,
                user_name=user.name,
                user_image=user.image,
                name=name.strip(),
                summary=summary.strip(),
                content=content.strip())
    await blog.save()
    return blog
