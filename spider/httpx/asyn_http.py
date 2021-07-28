import asyncio
import httpx
import threading
import time

client = httpx.AsyncClient()


async def async_main(url, sign):
    response = await client.get(url)
    status_code = response.status_code
    print(f'async_main: {threading.current_thread()}: {sign}:{status_code}')


loop = asyncio.get_event_loop()
tasks = [async_main(url='http://www.baidu.com', sign=i) for i in range(200)]
async_start = time.time()
loop.run_until_complete(asyncio.wait(tasks))
async_end = time.time()
loop.close()
print(async_end - async_start)


class _TypingEllipsis:
    pass


class _TypingEmpty:
    pass


params = list()
a = tuple(... if a is _TypingEllipsis else () if a is _TypingEmpty else a for a in params)



