From python

Run pip install aiohttp aiohttp-sse

Workdir /

Expose 8080
Cmd python -m aiohttp.web -H 0.0.0.0 app:init
