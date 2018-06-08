#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/5/20 19:51
# @Author  : zhouyuyao
# @File    : demon2.py
import multiprocessing
import time
import os

def worker(args, interval):           # interval 表示间隔
    print("start worker {0}({1})".format(args, os.getpid()))
    time.sleep(interval)
    print("end worker {0}({1})".format(args, os.getpid()))

def main():
    print("start main")
    print('Parent process {0}.'.format(os.getpid()))
    p1 = multiprocessing.Process(target=worker, args=(1,1))
    print('Parent process {0}.'.format(os.getpid()))
    p2 = multiprocessing.Process(target=worker, args=(2,2))
    print('Parent process {0}.'.format(os.getpid()))
    p3 = multiprocessing.Process(target=worker, args=(3,3))
    p1.start()
    p2.start()
    p3.start()
    print("end main")

if __name__ == '__main__':
    main()

'''
start main
Parent process 6180.
Parent process 6180.
Parent process 6180.
end main
start worker 1(17596)
start worker 2(5872)
start worker 3(19228)
end worker 1(17596)
end worker 2(5872)
end worker 3(19228)
'''

# p = multiprocessing.Process(target=, args=)
# target   指定的是当进程执行时，需要执行的函数
# args     是当进程执行时，需要给函数传入的参数
# 注意： args必须是一个tuple, 特别是当函数需要传入一个参数时 (1,)
# p 代表的是一个多进程，
# p.is_alive()     判断进程是否存活
# p.run()          启动进程
# p.start()        启动进程，他会自动调用run方法，推荐使用start
# p.join(timeout)  等待子进程结束或者到超时时间
# p.terminate()    强制子进程退出
# p.name           进程的名字
# p.pid            进程的pid