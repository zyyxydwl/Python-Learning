#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/1/22 23:13
# @Author  : zhouyuyao
# @File    : demonTuple.py
# PyCharm 2017.3.2 (Community Edition)
# Build #PC-173.4127.16, built on December 19, 2017
# JRE: 1.8.0_152-release-1024-b8 amd64
# JVM: OpenJDK 64-Bit Server VM by JetBrains s.r.o
# Windows 10 10.0
# Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) 
# [MSC v.1900 64 bit (AMD64)] on win32

l=list()
print(l)
t=tuple()
print(t)


a1=(1)
a2=(1,)
print(type(a1))
# <class 'int'>
print(type(a2))
# <class 'tuple'>


m = (1,2,3,43,4,6,1,3,4,4)
# count(value)     统计value的个数
print(m.count(1))
# 2
# index(value)     返回第一个value元素的下标
print(m.index(4))
# 4
print(m.index(2))
# 1
