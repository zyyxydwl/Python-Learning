#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/5/20 21:31
# @Author  : zhouyuyao
# @File    : demon4.py
import multiprocessing

def worker_with(lock, f):
    with lock:
        with open('file.txt',"a+") as fs:
            fs.write('Lock acquired via with\n')
        # fs.close()

def worker_no_with(lock, f):
    lock.acquire()
    '''
    This method blocks until the lock is unlocked, then sets it to
            locked and returns True.
    '''
    try:
        # fs = open(f, "a+")
        with open('file.txt',"a+") as fs:
            fs.write('Lock acquired directly\n')
    finally:
        lock.release()
        """Release a lock.

        When the lock is locked, reset it to unlocked, and return.
        If any other coroutines are blocked waiting for the lock to become
        unlocked, allow exactly one of them to proceed.

        When invoked on an unlocked lock, a RuntimeError is raised.

        There is no return value.
        """

def main():
    f = "file.txt"

    lock = multiprocessing.Lock()
    w = multiprocessing.Process(target=worker_with, args=(lock, f))
    nw = multiprocessing.Process(target=worker_no_with, args=(lock, f))

    w.start()     # p.start() 启动进程，他会自动调用run方法，推荐使用start
    nw.start()

    w.join()      # p.join(timeout) 等待子进程结束或者到超时时间
    nw.join()

if __name__ == "__main__":
    main()

