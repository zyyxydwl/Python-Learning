#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/1/24 21:29
# @Author  : zhouyuyao
# @File    : countnums.py
# PyCharm 2017.3.2 (Community Edition)
# Build #PC-173.4127.16, built on December 19, 2017
# JRE: 1.8.0_152-release-1024-b8 amd64
# JVM: OpenJDK 64-Bit Server VM by JetBrains s.r.o
# Windows 10 10.0
# Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) 
# [MSC v.1900 64 bit (AMD64)] on win32

status=1
while status:
    strings = input("Please input a string('quit' will exit):")
    if strings == "quit":
        exit(1)
    digit = pha = space = other = 0
    for i in strings:
        if i.isdigit():         # 检测字符串是否只由数字组成，包含则返回True，不包含为False
            digit +=1
        elif i.isalpha():       # 检测字符串是否只由字母组成，包含则返回True，不包含为False
            pha +=1
        elif i.isspace():       # 检测字符串是否只由空格组成，包含则返回True，不包含为False
            space +=1
        else:
            other +=1
    print("该字符串中数字有{0}个，字母有{1}个，空格有{2}个，其他{3}个。".format(digit,pha,space,other))
