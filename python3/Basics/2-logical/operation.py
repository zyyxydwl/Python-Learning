#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/1/23 21:41
# @Author  : zhouyuyao
# @File    : operation.py
# PyCharm 2017.3.2 (Community Edition)
# Build #PC-173.4127.16, built on December 19, 2017
# JRE: 1.8.0_152-release-1024-b8 amd64
# JVM: OpenJDK 64-Bit Server VM by JetBrains s.r.o
# Windows 10 10.0
# Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) 
# [MSC v.1900 64 bit (AMD64)] on win32
'''
编程语言最重要的是思想
ABCD乘以9=DCBA，求A=？，B=？，C=？，D=？
'''

for A in range(1,10):
    for B in range(0,10):
        for C in range(0,10):
            for D in range(1,10):
                start = 1000*A+100*B+10*C+D
                end = 1000*D+100*C+10*B+A
                if start * 9 == end:
                    print("A={}".format(A))
                    print("B={}".format(B))
                    print("C={}".format(C))
                    print("D={}".format(D))
                    print("{0} * 9 = {1}".format(start,end))
