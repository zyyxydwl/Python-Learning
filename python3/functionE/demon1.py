#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/1/28 21:56
# @Author  : zhouyuyao
# @File    : demon1.py
# PyCharm 2017.3.2 (Community Edition)
# Build #PC-173.4127.16, built on December 19, 2017
# JRE: 1.8.0_152-release-1024-b8 amd64
# JVM: OpenJDK 64-Bit Server VM by JetBrains s.r.o
# Windows 10 10.0
# Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) 
# [MSC v.1900 64 bit (AMD64)] on win32

def add(args):
    total = 0
    for i in args:
        total += i
    return total

def main():
    number = list()
    s = input("Please input digit like(a+b+c+d): ")
    for num in s.split("+"):     # 以+号为分隔符切割s字符串
        number.append(int(num.strip())) # num.strip() 去除前后的空格
    print(add(number))         # 最后得到的字符串 number 调用add函数

if __name__ == "__main__":     # 直接调用主函数
    main()


