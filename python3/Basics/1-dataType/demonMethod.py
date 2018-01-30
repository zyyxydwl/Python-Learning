#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/1/23 0:13
# @Author  : zhouyuyao
# @File    : demonMethod.py
# PyCharm 2017.3.2 (Community Edition)
# Build #PC-173.4127.16, built on December 19, 2017
# JRE: 1.8.0_152-release-1024-b8 amd64
# JVM: OpenJDK 64-Bit Server VM by JetBrains s.r.o
# Windows 10 10.0
# Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) 
# [MSC v.1900 64 bit (AMD64)] on win32

# help()       ctrl + 鼠标左键
s="dedwefwfrgwr"
# help(s.split())
result = s.startswith("de")
print(result)
# True


# dir()
print(dir(s))
# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__',
# '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
# '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__',
# '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__',
# '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
#  '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__',
# '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center',
# 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format',
# 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit',
#  'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace',
# 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans',
#  'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition',
# 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip',
# 'swapcase', 'title', 'translate', 'upper', 'zfill']


# type()
a="123"
print(type(a))
# <class 'str'>
print(type(int(a)))
# <class 'int'>


# isinstance(a,type)  返回值是一个bool类型
print(isinstance(s,str))
# True
print(isinstance(s,dict))
# False


