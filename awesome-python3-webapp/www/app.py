import logging
import asyncio
from aiohttp import web
logging.basicConfig(level=logging.INFO)


def index(request):
    return web.Response(body='你好'.encode(encoding='utf-8'),
                        headers={'Content-Type': 'text/html;charset=utf-8'})


@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route("GET", "/", index)
    srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('Server started at http://127.0.0.1:9000')
    return srv


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
