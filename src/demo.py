from aiohttp import web

async def api_version(request):
    return web.Response(text="1")

app = web.Application()
app.add_routes([web.get('/', api_version)])

if __name__ == '__main__':
    web.run_app(app)
