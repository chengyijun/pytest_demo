# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: process_thread_coroutine.py
@time: 2020/8/14 9:34
@desc:
"""
import asyncio
import multiprocessing
import threading
from multiprocessing import Process
from threading import Thread


class MyCoroutine:
    async def task(self, n):
        await asyncio.sleep(n)
        # print(f'我是task 耗时{n}秒')
        print(f'我是 {multiprocessing.current_process().name} 中的 线程 {threading.current_thread().getName()} 中的 {n}号协程')

    def async_test(self):
        new_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(new_loop)
        # 1. 建立一个事件循环
        loop = asyncio.get_event_loop()
        # 2. 将异步函数加入事件队列
        # tasks = [task(1), task(2), task(3)]
        tasks = [asyncio.ensure_future(self.task(i)) for i in range(1, 4)]
        # 3. 执行事件队列至任务结束
        loop.run_until_complete(asyncio.wait(tasks))
        # 4. 关闭事件循环
        loop.close()


class MyProcess(Process):

    def task(self):
        ts = []
        for i in range(2):
            t = MyThread()
            ts.append(t)
            t.start()
        for t in ts:
            t.join()

    def run(self):
        self.task()


class MyThread(Thread):
    count = 0

    def task(self):
        mc = MyCoroutine()
        mc.async_test()

    def run(self):
        self.task()


def main():
    cpu_count = multiprocessing.cpu_count()
    for i in range(2):
        mp = MyProcess(name=f'进程{i + 1}')
        mp.start()
    print('主进程结束')


if __name__ == '__main__':
    main()
