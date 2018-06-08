#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/5/20 23:10
# @Author  : zhouyuyao
# @File    : demon7.py
from multiprocessing import Process,Value,Array
def f(n,a):
        n.value = 3.1415926
        for i in range(len(a)):
                a[i] = -a[i]
def main():
    num = Value('d', 0.0)
    arr = Array('i', range(10))
    p = Process(target=f, args=(num, arr))
    p.start()
    p.join()
    print(num.value)
    print(arr[:])

if __name__ == "__main__":
    main()
