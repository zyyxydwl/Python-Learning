#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/1/23 22:09
# @Author  : zhouyuyao
# @File    : Factorial.py
# PyCharm 2017.3.2 (Community Edition)
# Build #PC-173.4127.16, built on December 19, 2017
# JRE: 1.8.0_152-release-1024-b8 amd64
# JVM: OpenJDK 64-Bit Server VM by JetBrains s.r.o
# Windows 10 10.0
# Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) 
# [MSC v.1900 64 bit (AMD64)] on win32

# 求1-n的阶乘的和
# 1！+ 2！+ 3！+ 4！+5 ！+ ··· + n！
# 0! = 1
# 1！= 1
# 2！= 1 * 2 = 2
# 3！= 1 * 2 * 3 = 6

def one(n):
    total = 1
    if n ==0:
        total = 1
    else:
        for i in range(1,n+1):
            total *= i
    return total
print(one(3))


status=1
while status:
    result = 0
    n= input("Please input a number(n>=0) : ")
    for i in n:
        if not i.isdigit():
            print("The number of you input is error.")
            exit(1)
    if int(n) < 0:
        print("The number of you input is error.")
        break
    for i in range(0,int(n)+1):
        result += one(i)
    print("0! + 1! + 2! + ··· ··· + n! = {}".format(result))

