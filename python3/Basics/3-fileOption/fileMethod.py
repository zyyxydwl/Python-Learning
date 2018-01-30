#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/1/25 22:02
# @Author  : zhouyuyao
# @File    : fileMethod.py
# PyCharm 2017.3.2 (Community Edition)
# Build #PC-173.4127.16, built on December 19, 2017
# JRE: 1.8.0_152-release-1024-b8 amd64
# JVM: OpenJDK 64-Bit Server VM by JetBrains s.r.o
# Windows 10 10.0
# Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) 
# [MSC v.1900 64 bit (AMD64)] on win32
import codecs

ENCODING = "utf-8"       # 字符集
f = open("z.log",encoding=ENCODING)
print(f.name)            # 文件名
print(f.readline())      # 读取成列表的形式
print(f.readlines())     # 读取成列表的形式

with codecs.open("z.log","r",encoding=ENCODING) as f:
    print(f.read())



