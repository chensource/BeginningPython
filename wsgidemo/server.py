from wsgiref.simple_server import make_server
from index import application

httpd = make_server('', 8095, application)
print('Server HTTP on port 8095...')

httpd.serve_forever()
