#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      : 2017/12/13 22:16
# @Author    : zhouyuyao
# @File      : oneEXP.py

# 多核CPU是使用多进程。
# python中提供了threading模块来对多线程进行操作，线程是应用程序中工作的最小单元。
#
# 使用多线程有两种方式：
# 1、将要执行的方法作为参数传给thread的构造方法，和多进程类似
# 2、从thread继承，并重写run()


import threading

from function.demo import args


def worker(n):
    print("start worker{0}".format(n))

class MyThread(threading.Thread):
    def __init__(self,args):
        super(MyThread,self).__init__()
        self._args=args
    def run(self):    # 重写run
        print("start MyThread{0}".format(self,args))

if __name__ == "__main__":      # 如果名字等于主函数
    for i in range(1,7):
        t1=threading.Thread(target=worker,args=(i,))
        t1.start()
        t1.join()

    for x in range(7,11):
        t2=MyThread(x)
        t2.start()
        t2.join()

