'''
    1.先调用服务
    2.解析json格式的数据
'''

# import json
# import request from http
# import urllib

# BASE_URL = 'http://10.4.18.82/core/022/json/reply/GetGScopesRequest'
# req = urllib.request.Request(BASE_URL)
# content = req.read()
# if (content):
#     print(json(content))

import sys, json
import urllib.request
BASE_URL = 'http://10.4.18.82/core/022/json/reply/GetGScopesRequest'
req = urllib.request.Request(BASE_URL)
resp = urllib.request.urlopen(req)
content = resp.read()
if (content):
    print(content.decode('utf-8'))
