# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: process_thread.py
@time: 2020/8/14 9:34
@desc: 多进程-多线程模型
"""
import multiprocessing
import threading
import time
from multiprocessing import Process
from threading import Thread


class MyProcess(Process):

    def task(self):
        ts = []
        for i in range(10):
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
        time.sleep(2)
        print(f'我是 {multiprocessing.current_process().name} 中的 线程 {threading.current_thread().getName()}')

    def run(self):
        while True:
            self.task()
            self.count += 1
            if self.count == 100:
                break


def main():
    cpu_count = multiprocessing.cpu_count()
    for i in range(cpu_count):
        mp = MyProcess(name=f'进程{i + 1}')
        mp.start()


if __name__ == '__main__':
    main()
