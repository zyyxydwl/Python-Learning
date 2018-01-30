#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/1/23 21:21
# @Author  : zhouyuyao
# @File    : demonIf.py
# PyCharm 2017.3.2 (Community Edition)
# Build #PC-173.4127.16, built on December 19, 2017
# JRE: 1.8.0_152-release-1024-b8 amd64
# JVM: OpenJDK 64-Bit Server VM by JetBrains s.r.o
# Windows 10 10.0
# Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) 
# [MSC v.1900 64 bit (AMD64)] on win32

# python 缩进
# main：
#   print("Hello")
#print("Hello world.")

if 判断条件:
    执行语句
elif 判断条件:
    执行语句
else:
    执行语句

while 判断条件:
    执行语句

a = 100
while a>1:
    print(a)
    a-=1
    if a==50:
        break   # 退出循环
    if a==55:
        print("5555555555")
        continue   # 此次循环结束，进入下一个循环

# break  跳出循环
# continue  进入下一次循环


# for item in sequence：
#   执行语句

l = ["a","b","c","d","e","f"]
print(l[:])
print(l[0:5])        # 大于等于0     小于5  0 <= a > 5
print(l[0:-1])        # 大于等于0     小于5  0 <= a > 5
for x,y in enumerate(l):    # 打印列表中元素以及下标
    print(x,y)






















