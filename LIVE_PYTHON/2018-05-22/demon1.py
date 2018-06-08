#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/5/23 14:15
# @Author  : zhouyuyao
# @File    : demon1.py
import multiprocessing
import os
import time
from datetime import datetime

def subprocess(number):
    # 子进程
    print('这是第{0}个子进程'.format(number))
    pid = os.getpid()              # 得到当前进程号
    print('当前进程号：{0}，开始时间：{1}'.format(pid, datetime.now().isoformat()))
    time.sleep(30)                 # 当前进程休眠30秒
    print('当前进程号：{0}，结束时间：{1}'.format(pid, datetime.now().isoformat()))

def mainprocess():
    # 主进程
    print('这是主进程，进程编号：{0}'.format(os.getpid()))
    t_start = datetime.now()
    pool = multiprocessing.Pool()
    for i in range(8):
        pool.apply_async(subprocess, args=(i,))
    pool.close()
    pool.join()
    t_end = datetime.now()
    print('主进程用时：{0}毫秒'.format((t_end - t_start).microseconds))


if __name__ == '__main__':
    # 主测试函数
    mainprocess()