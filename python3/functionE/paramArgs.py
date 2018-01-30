#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/1/29 21:32
# @Author  : zhouyuyao
# @File    : paramArgs.py
# PyCharm 2017.3.2 (Community Edition)
# Build #PC-173.4127.16, built on December 19, 2017
# JRE: 1.8.0_152-release-1024-b8 amd64
# JVM: OpenJDK 64-Bit Server VM by JetBrains s.r.o
# Windows 10 10.0
# Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) 
# [MSC v.1900 64 bit (AMD64)] on win32

def add(*args):
    total = 0
    for i in args:
        total += i
    print("total = {}".format(total))

def sorDictValue(dict1):
    print(sorted(dict1.items(),key=lambda item:item[0],reverse=False))
'''sorted后面接dict1表示迭代key值，
如果加入dict1.items（）函数表示字典的keys和value值都将进行迭代'''


if __name__ == '__main__':
    add(1,2,3,4,5)
    s1 = lambda x,y:x+y
    print(s1(10,20))
    aaa = dict(a=100,b=10,c=50)
    l = list()
    sorDictValue(aaa)



# 匿名函数，就是没有名字的函数，但是为什么又需要匿名函数呢，它的作用又是什么
# lambda函数是一种快速定义单行的最小函数，可以用在任何需要函数的地方

def fun(x,y):
    return x*y

# lambda 版本
r = lambda x,y:x*y
print(r(10,20))









