from .infer import generate as gen_func
from aiohttp import web
from aiohttp_sse import sse_response
from urllib.parse import unquote, quote

import base64
import os


async def generate(request: web.Request) -> web.Response:
    message = request.query.get('prompt', '')
    prompt = base64.b64decode(message.encode()).decode()
    prompt = unquote(prompt)
    text = await request.text()
    async with sse_response(request) as resp:
        for o in gen_func(prompt):
            await resp.send(o)
        return resp


async def reply(request: web.Request) -> web.Response:
    data = await request.json()
    prompt = data.get('prompt', '')
    rsp = ''.join(gen_func(prompt))
    return web.Response(text=rsp)


async def infer(request: web.Request) -> web.Response:
    data = await request.json()
    prompt = data.get('prompt', '')
    prompt = quote(prompt)
    message = base64.b64encode(prompt.encode()).decode()
    return web.HTTPFound(f'/generate?prompt={message}')


async def index(request):
    return web.HTTPFound('/index.html')


def init(argb):
    app = web.Application()
    app.router.add_post('/infer', infer)
    app.router.add_post('/generate', reply)
    app.router.add_get('/generate', generate)
    app.router.add_get('/', index)
    app.router.add_static('/', os.path.dirname(__file__))
    return app
