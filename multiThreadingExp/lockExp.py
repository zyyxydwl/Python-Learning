#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      : 2017/12/13 22:51
# @Author    : zhouyuyao
# @File      : lockExp.py
import threading
import time
def worker(name, lock):
    with lock:
        print("start {0}".format(name))
        time.sleep(5)
        print("end {0}".format(name))
if __name__ == "__main__":
    lock = threading.Lock()
    t1 = threading.Thread(target=worker, args=("worker1", lock))
    t2 = threading.Thread(target=worker, args=("worker2", lock))
    t1.start()
    t2.start()
    print("main end.")
