#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      : 2017/12/15 20:05
# @Author    : zhouyuyao
# @File      : queueExp.py

# 消息队列是在消息传输过程中保存消息的容器。
# 消息队列最近的的用法就是消费者和生成者之间通过消息管道来传递消息
# 消费者和生成者是不同的进程，生产者往管道中写消息，消费者从管道中读消息
# 操作系统提供了很多机制来实现进程间的通信，
# multiprocessing模块提供了queue和pipe两种方法来实现
import queue
from multiprocessing import Process,Queue
def write(q):
    for i in ["a", "b", "c", "d"]:
        q.put(i)
        print("put {0} to queue".format(i))

def read(q):
    while 1:
        result = q.get()
        print("get {0} from queue".format(result))

def main():
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()

if __name__ == '__main__':
    main()