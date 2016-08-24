from urllib import request,parse

URL_INDEX = 'http://www.douban.com'
URL_LOGIN = 'https://passport.weibo.cn/sso/login'
# with request.urlopen(URL_INDEX) as f:
#     data = f.read()
#     print('status:', f.status, f.reason)
#     for key, value in f.getheaders():
#         print('%s:%s' % (key, value))
#     print('data:', data.decode('utf-8'))

#Get 请求
# req = request.Request(URL_INDEX)
# req.add_header(
#     'User-Agent',
#     'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# with request.urlopen(URL_INDEX) as f:
#     data = f.read()
#     print('status:', f.status, f.reason)
#     for key, value in f.getheaders():
#         print('%s:%s' % (key, value))
#     print('data:', data.decode('utf-8'))

print('Login in Weibo...')
email = input('Email:')
password = input('Password:')
login_data = parse.urlencode([
    ('username', email), ('password', password), ('entry', 'mweibo'),
    ('client_id', ''), ('savestate', '1'), ('ec', ''),
    ('pagerefer',
     'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F'
     )
])

req = request.Request(URL_LOGIN)
req.add_header('Origin', 'https://passwort.weibo.cn')
req.add_header(
    'User-Agent',
    'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header(
    'referer',
    'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

with request.urlopen(req, data=login_data.encode('utf-8')) as f:
    # print("Status: ", f.status, f.reason)
    # for key, value in f.getheaders():
    #     print('%s:%s' % (key, value))
    # print('Data:', f.read().decode('utf-8'))
    f.read().decode('utf-8')

class RailLine(object):
    def __init__(self,RailLineID,RailLineName):
        self.RailLineID = RailLineID
        self.RailLineName = RailLineName
