#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/5/23 21:49
# @Author  : zhouyuyao
# @File    : demon2.py
import threading

def worker(args):
    print("开始子线程 {0}".format(args))
    print("结束子线程 {0}".format(args))

if __name__ == '__main__':

    print("start main")
    t1 = threading.Thread(target=worker, args=(1,))
    t2 = threading.Thread(target=worker, args=(2,))
    t1.start()
    t2.start()
    print("end main")