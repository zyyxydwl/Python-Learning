#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/1/24 21:39
# @Author  : zhouyuyao
# @File    : Multiplication.py
# PyCharm 2017.3.2 (Community Edition)
# Build #PC-173.4127.16, built on December 19, 2017
# JRE: 1.8.0_152-release-1024-b8 amd64
# JVM: OpenJDK 64-Bit Server VM by JetBrains s.r.o
# Windows 10 10.0
# Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) 
# [MSC v.1900 64 bit (AMD64)] on win32

for i in range(1,10):
    for j in range(1,i+1):
        print("{0} x {1} = {2}".format(j,i,i*j),end="")
        if i ==j:
            print("")
