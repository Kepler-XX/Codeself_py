"""
进程 线程 协程  进程池 线程池 协程池
"""
# 进程
import asyncio
import time
from threading import Thread
# 线程
from multiprocessing import Process

# 进程池 线程池
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def fn(name):
    for i in range(100):
        print(f'thread--{i}-{name}')


async def fn1():
    print('hello world')
    # time.sleep(3)  # 本质还是同步操作 IO需等待
    await asyncio.sleep(3)
    print('hello python')


async def fn2():
    print('你好，世界')
    # time.sleep(2)
    await asyncio.sleep(2)
    print('你好 python')


async def fn3():
    print('hello start')
    # time.sleep(4)
    await asyncio.sleep(4)
    print('hello end')


async def main():
    tasks = [
        asyncio.create_task(fn1()),
        asyncio.create_task(fn2()),
        asyncio.create_task(fn3())
    ]
    await asyncio.wait(tasks)


if __name__ == '__main__':
    # Thread(target=fn, args=("test",)).start()  # 进程使用方式
    # Process(target=fn, args=("test",)).start()  # 线程使用方式

    # 线程池
    # with ThreadPoolExecutor(50) as t:
    #     for i in range(20):
    #         t.submit(fn, name='7788')

    # 进程池
    # with ProcessPoolExecutor(20) as p:
    #     for i in range(10):
    #         p.submit(fn, name='8899')
    # print('thread over!')

    # 异步协程
    t1 = time.time()
    asyncio.run(main())
    t2 = time.time()
    print(t2 - t1)  # time.sleep 总耗时9.024957418441772
    # awit asyncio.sleep 总耗时4.00711989402771
