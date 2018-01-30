#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/1/25 20:49
# @Author  : zhouyuyao
# @File    : demonWrite.py
# PyCharm 2017.3.2 (Community Edition)
# Build #PC-173.4127.16, built on December 19, 2017
# JRE: 1.8.0_152-release-1024-b8 amd64
# JVM: OpenJDK 64-Bit Server VM by JetBrains s.r.o
# Windows 10 10.0
# Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) 
# [MSC v.1900 64 bit (AMD64)] on win32



if __name__== "__main__":
    filename = input("Please input the name of file:")
    f = open(filename,"w")     # 以写的形式打开一个文件
    while 1:         # 1 的效率是最高的
        context = input("Please input context('EOF' will close file): ")
        if context == "EOF":
            f.close()
            break
        else:
            f.write(context)
            f.write("\n")

    fRead = open(filename)
    readContext = fRead.read()
    print("------------start-------------")
    print(readContext)
    print("-------------end--------------")
    fRead.close()



