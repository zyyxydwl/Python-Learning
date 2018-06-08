#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/5/24 20:49
# @Author  : zhouyuyao
# @File    : demon1.py


'''
1、消息队列有哪些？
2、专门用于Python的消息队列，只要学习它的思想
3、pipe
4、celery

'''

import time
import queue
import threading


def worker(i):
    while True:
        item = q.get()
        if item is None:
            print("线程%s发现了一个None,可以休息了^-^" % i)
            break
        # do_work(item)做具体的工作
        time.sleep(0.5)
        print("线程%s将任务<%s>完成了！" % (i, item))
        # 做完后发出任务完成信号，然后继续下一个任务
        q.task_done()

if __name__ == '__main__':
    num_of_threads = 5
    source = [i for i in range(1, 21)]  # 模拟20个任务
    # 创建一个FIFO队列对象，不设置上限
    q = queue.Queue()
    # 创建一个线程池
    threads = []
    # 创建指定个数的工作线程，并讲他们放到线程池threads中
    for i in range(1, num_of_threads + 1):
        t = threading.Thread(target=worker, args=(i,))
        threads.append(t)
        t.start()

    # 将任务源里的任务逐个放入队列
    for item in source:
        time.sleep(0.5)  # 每隔0.5秒发布一个新任务
        q.put(item)

    # 阻塞队列直到队列里的任务都完成了
    q.join()
    print("-----工作都完成了-----")
    # 停止工作线程
    for i in range(num_of_threads):
        q.put(None)
    for t in threads:
        t.join()
    print(threads)






