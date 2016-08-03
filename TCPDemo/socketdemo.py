import socket
import threading
import time

'抓取页面'
#创建一个socket TCP/IP 协议
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect(('bj.centanet.com', 80))
# s.send(b'GET / HTTP/1.1\r\n Host:nj.centanet.com \r\nConnection:close\r\n\r\n')
#
# buffer = [] gan
#
# while True:
#     d = s.recv(1024)
#     if d:
#         buffer.append(d)
#     else:
#         break
# data = b''.join(buffer)
# s.close()
#
# header, html = data.split(b'\r\n\r\n', 1)
# print(header.decode('utf-8'))
#
# with open('index_nj.html', 'wb') as f:
#     f.write(html)

'服务器监听端口'
#创建一个基于TCP/IP 协议的 Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 监听端口
s.bind(('127.0.0.1', 9999))

#最大监听数量
s.listen(5)
print('Waiting for connection...')


def tcplink(sock, addr):
    print('Accept new connection from %s:%s..' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('hello,%s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed!' % addr)


while True:
    sock, addr = s.accept()
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
