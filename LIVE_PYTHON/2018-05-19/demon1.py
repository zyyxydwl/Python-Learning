#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/5/19 20:09
# @Author  : zhouyuyao
# @File    : 2018-05-19.py


'''
1、Linux上如何查看线程  ps -efL
外面是进程，里面是线程，进程是包含线程的
2、shell 里面用什么来表示多线程

'''

import multiprocessing
import os

# 子进程要执行的代码
def run_proc(name):
    print('Run child process {0} ({1})...'.format(name, os.getpid()))

def parent_process():
    print('Parent process {0}.'.format(os.getpid()))
    p = multiprocessing.Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')

if __name__=='__main__':
    parent_process()



