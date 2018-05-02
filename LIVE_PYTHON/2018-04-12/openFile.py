#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/4/12 20:56
# @Author  : zhouyuyao
# @File    : openFile.py
# PyCharm 2017.3.2 (Community Edition)
# Build #PC-173.4127.16, built on December 19, 2017
# JRE: 1.8.0_152-release-1024-b8 amd64
# JVM: OpenJDK 64-Bit Server VM by JetBrains s.r.o
# Windows 10 10.0
# Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) 
# [MSC v.1900 64 bit (AMD64)] on win32

# 读取文件
# f=open('111.log','r')
import codecs

f=open('111.log','r',encoding='utf-8')  # 必须指定 encoding 编码
print(f.read())
f.close()

# 在Python3中对文件进行操作时，不指定编码可能出现如下错误
# C:\Users\admin\AppData\Local\Programs\Python\Python36\python.exe E:/GitHub/Python-Learning/LIVE_PYTHON/2018-04-12/openFile.py
# Traceback (most recent call last):
#   File "E:/GitHub/Python-Learning/LIVE_PYTHON/2018-04-12/openFile.py", line 17, in <module>
#     print(f.read())
# UnicodeDecodeError: 'gbk' codec can't decode byte 0x80 in position 48: illegal multibyte sequence


# 写入文件
f1=open('222.log','a',encoding='utf-8')  # 必须指定 encoding 编码
f1.write("总部	剁椒鱼头（半只）	泡红椒1*2.5kg	125	125	7	克	1.75\n")
f1.close()

# 全局申明编码格式
# ENCODING="utf-8"
# fExp=open('222.log','w',encoding=ENCODING)  # 必须指定 encoding 编码


f=open('111.log','r',encoding='utf-8')  # 必须指定 encoding 编码
for  line  in f.readlines():
    print(line)

# f.name  文件名字
# f.fileno() 文件描述符
# f.close() 关闭文件
# f.encoding() 文件编码
# f.closed() 返回bool值，判断文件是否已经关闭

# 读写文件后自动关闭文件
with codecs.open('222.log','r',encoding='utf-8') as z:
    print(z.read())       # 返回字符串 <class 'str'>
    print(z.readlines())  # 返回列表 <class 'list'>


# 函数
# 形参
# 实参

