# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: aiohttp_demo.py
@time: 2020/8/14 9:04
@desc:
"""
import asyncio
import time

from aiohttp import ClientSession

tasks = []
url = "https://www.baidu.com/{}"


async def hello(url):
    async with ClientSession() as session:
        async with session.get(url) as response:
            response = await response.read()
            #            print(response)
            print('Hello World:%s' % time.time())


def run():
    for i in range(5):
        task = asyncio.ensure_future(hello(url.format(i)))
        # task = hello(url.format(i))
        tasks.append(task)


def main():
    loop = asyncio.get_event_loop()
    run()
    loop.run_until_complete(asyncio.wait(tasks))


if __name__ == '__main__':
    main()
