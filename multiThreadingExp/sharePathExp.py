#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      : 2017/12/14 23:13
# @Author    : zhouyuyao
# @File      : sharePathExp.py

# 15.3 多线程共享变量
# 多进程之间是相互独立的，而多线程本身是与父进程共享内存的;
# 这也是为什么一个线程挂掉之后，其他线程也会挂的道理。
import threading
l = list()
l+=range(1,10)
print(l)
def worker():
    l.append("zhou")
    l.append("yu")
    l.append("yao")
if __name__ == "__main__":
    t=threading.Thread(target=worker)
    t.start()
    print(l)
