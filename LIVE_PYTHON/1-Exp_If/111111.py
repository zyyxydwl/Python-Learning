#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/4/12 9:39
# @Author  : zhouyuyao
# @File    : 111111.py
# PyCharm 2017.3.2 (Community Edition)
# Build #PC-173.4127.16, built on December 19, 2017
# JRE: 1.8.0_152-release-1024-b8 amd64
# JVM: OpenJDK 64-Bit Server VM by JetBrains s.r.o
# Windows 10 10.0
# Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) 
# [MSC v.1900 64 bit (AMD64)] on win32

while 1:
    strings = input("Please inpur a string(quit will be exit):")
    alpha, dig, space, other = 0, 0, 0, 0
    if strings.strip() == "quit":
        exit(1)
    for i in strings:
        if i.isdigit():
            dig += 1
        elif i.isspace():
            space += 1
        elif i.isalpha():
            alpha += 1
        else:
            other += 1
    print("alpha = {0}".format(alpha))
    print("dig = {0}".format(dig))
    print("space = {0}".format(space))
    print("other = {0}".format(other))
