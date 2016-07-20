from http.server import BaseHTTPRequestHandler, HTTPServer
import time

HOST_NMAE = '10.58.8.217'
PORT_NUMBER = 889


class MyServer(BaseHTTPRequestHandler):
    # print('''处理请求页面''')

    #页面模板
    # page = '''\<html><body><p>hello,world</p></body></html>'''

    #处理一个Get请求
    def do_GET(self):
        self.send_response(200)
        self.send_hander("Content-Type", "text/html")
        self.send_hander("Content-Length", str(len(self.page)))
        self.end_handers()
        #Send the html message
        self.wfile.write(bytes(
            "<html><head><title>Title goes here.</title></head>", "utf-8"))
        self.wfile.write(bytes("<body><p>This is a test.</p>", "utf-8"))
        self.wfile.write(bytes("<p>You accessed path: %s</p>" % self.path,
                               "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

    # if __name__ == 'main':
    #     serverAddress = ('', PORT_NUMBER)
    #     server = BaseHTTPServer.HTTPServer(serverAddress, RequestHandler)
    #     server.server_forever()


myServer = HTTPServer((HOST_NMAE, PORT_NUMBER), MyServer)
print(time.asctime(), "Server Starts - %s:%s" % (HOST_NMAE, PORT_NUMBER))

try:
    myServer.server_forever()
except Exception as e:
    pass

print(time.asctime(), "Server Starts - %s:%s" % (HOST_NMAE, PORT_NUMBER))
