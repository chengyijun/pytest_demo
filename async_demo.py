# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: async_demo.py
@time: 2020/8/14 8:39
@desc:
"""
import asyncio
import time


async def task(n):
    await asyncio.sleep(n)
    print(f'我是task 耗时{n}秒')


def main():
    stime = time.time()
    async_test()
    etime = time.time()
    print(f'共耗时{etime - stime}')


def async_test():
    # 1. 建立一个事件循环
    loop = asyncio.get_event_loop()
    # 2. 将异步函数加入事件队列
    # tasks = [task(1), task(2), task(3)]
    tasks = [asyncio.ensure_future(task(i)) for i in range(1, 4)]
    # 3. 执行事件队列至任务结束
    loop.run_until_complete(asyncio.wait(tasks))
    # 4. 关闭事件循环
    loop.close()




if __name__ == '__main__':
    main()
