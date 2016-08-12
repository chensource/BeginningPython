# import asyncio


# @asyncio.coroutine
# def hello():
#     print("hello")
#     yield from asyncio.sleep(1)
#     print('hello again!')

# loop = asyncio.get_event_loop()
# loop.run_until_complete(hello())
# loop.close()

# import threading
# import asyncio


# @asyncio.coroutine
# def hello():
#     print('hello world! (%s)' % threading.currentThread())
#     yield from asyncio.sleep(1)
#     print('hello again! (%s)' % threading.currentThread())

# loop = asyncio.get_event_loop()
# tasks = [hello(), hello()]

# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()

import asyncio


@asyncio.coroutine
def getindex(host):
    print('Get website %s...' % host)
    connet = asyncio.open_connection(host, 80)
    render, writer = yield from connet
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    while True:
        line = yield from render.readline()
        if line == b'\r\n':
            break
        # print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    writer.close()

loop = asyncio.get_event_loop()
tasks = [getindex(host) for host in ['www.baidu.com',
                                     'tj.centanet.com', 'www.163.com',
                                     'www.sohu.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
