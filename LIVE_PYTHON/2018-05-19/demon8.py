#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/5/20 23:13
# @Author  : zhouyuyao
# @File    : demon8.py

from multiprocessing import Process,Manager

def f(d,l):
        # d[1] = '1'
        # d['2'] = 2
        # d[0.25] = None
        # l.reverse()
        # '''reverse() 函数用于反向列表中元素。
        # 该方法没有返回值，但是会对列表的元素进行反向排序'''
        for i in range(10):
            key = "args" + str(i)
            d[key] = i*i
        print(d)

def main():
    manager = Manager()
    d = manager.dict()
    # l = manager.list(range(10))
    l = manager.list()
    p = Process(target=f, args=(d, l))
    p.start()
    p.join()     # 父进程需要等待子进程结束
    print(d)
    print(l)

if __name__ == "__main__":
    main()
