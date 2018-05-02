#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/4/26 22:51
# @Author  : zhouyuyao
# @File    : demon1.py
# PyCharm 2017.3.2 (Community Edition)
# Build #PC-173.4127.16, built on December 19, 2017
# JRE: 1.8.0_152-release-1024-b8 amd64
# JVM: OpenJDK 64-Bit Server VM by JetBrains s.r.o
# Windows 10 10.0
# Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) 
# [MSC v.1900 64 bit (AMD64)] on win32

'''
加密  md5 rsa
hashlib
'''
import hashlib

md5 = hashlib.md5()
src1 = "have a".encode('utf-8')
src2 = "nice day".encode('utf-8')
# md5.update(src.encode('utf-8'))
md5.update(src1)
md5.update(src2)
print(md5.hexdigest())


# m3 = hashlib.md5("123456".encode("utf-8"))
# src = bytes("ling", encoding="utf-8")
# m3.update(src)
# print(m3.hexdigest())



