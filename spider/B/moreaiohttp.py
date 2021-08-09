import asyncio
import aiohttp
import os

path = os.getcwd()

urls = [
    'https://u.53pic.com/i/qq/20201125/q25xhu0yruh.jpg',
    'https://u.53pic.com/i/qq/20201125/nky24w20d55.jpg',
    'https://u.53pic.com/i/qq/20201125/khq5p4tirow.jpg',
    'https://u.53pic.com/i/qq/20201125/pr2raqv11wx.jpg',
    'https://u.53pic.com/i/mingxin/20201215/pqmew202ncq.jpg',
    'https://img2.baidu.com/it/u=48604988,2833794849&fm=26&fmt=auto&gp=0.jpg',
    'https://img1.baidu.com/it/u=135946475,2967770012&fm=26&fmt=auto&gp=0.jpg',
    'https://img1.baidu.com/it/u=1477054895,1169641709&fm=26&fmt=auto&gp=0.jpg'
]


async def downloadimg(url):
    name = url.rsplit('/', 1)[1]
    async with aiohttp.ClientSession() as s:
        async with s.get(url) as r:
            with open(path + '\\pleaseanswer1988' + '\\' + name, mode='wb') as f:
                f.write(await r.content.read())

    print('over!')


async def main():
    tasks = []
    for url in urls:
        tasks.append(downloadimg(url))
    await asyncio.wait(tasks)

if __name__ == '__main__':
    asyncio.run(main())