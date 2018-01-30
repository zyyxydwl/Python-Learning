#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/1/25 23:06
# @Author  : zhouyuyao
# @File    : sortUIDPasswd.py
# PyCharm 2017.3.2 (Community Edition)
# Build #PC-173.4127.16, built on December 19, 2017
# JRE: 1.8.0_152-release-1024-b8 amd64
# JVM: OpenJDK 64-Bit Server VM by JetBrains s.r.o
# Windows 10 10.0
# Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) 
# [MSC v.1900 64 bit (AMD64)] on win32
import codecs

file = "passwd"
sortfile = "sortpasswd.txt"
filecontext = []
sortuid = []

with codecs.open(sortfile,"wb") as fsort:
    with codecs.open(file,encoding="utf-8") as f:
        filecontext += f.readlines()
        for line in filecontext:
            sortuid.append(int(line.split(":")[2]))
        sortuid.sort()
        for uid in sortuid:
            for line in filecontext:
                if str(uid) == line.split(":")[2]:
                    print(line)
                    fsort.write(line.encode("utf-8"))
# python3的新特性对文本和二进制数据作了更为清晰的区分，
# 文本总是Unicode，由str类型表示，
# 二进制则是由bytes类型表示
# 字符串可以encode编码成字节包，而字节包可以decode解码成字符串
