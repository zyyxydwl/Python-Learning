#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/1/29 22:46
# @Author  : zhouyuyao
# @File    : production.py
# PyCharm 2017.3.2 (Community Edition)
# Build #PC-173.4127.16, built on December 19, 2017
# JRE: 1.8.0_152-release-1024-b8 amd64
# JVM: OpenJDK 64-Bit Server VM by JetBrains s.r.o
# Windows 10 10.0
# Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) 
# [MSC v.1900 64 bit (AMD64)] on win32

# 列表生成式
a = [x*x for x in range(1,30) if x%2 ==0]
print(a)
print(type(a))
# <class 'list'>

y=list()
x=[1,2,3,4,5]
y+=x
y.append(100)
print(y)
print(x)

# 列表生成器 generator
b = (x*x for x in range(1,30) if x%2 ==0)
print(b)
print(type(b))
# <class 'generator'>

def test(l):
    for i in l:
        yield i        # yield 相当于return
        print("i = {}".format(i))

m = test([1,2,3,4,5,6,7,8,9])
print(type(m))
# <class 'generator'>

# 列表生成式直接返回了表达式的结果列表，
# 而生成器是一个对象，该对象包含了对表达式结果的计算引用，通过循环可以直接输出
# 生成器不会一次性列出所有的数据，当你用到的时候再列出来，这样降低了内存使用率







