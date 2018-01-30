#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/1/21 17:50
# @Author  : zhouyuyao
# @File    : listExp.py
# PyCharm 2017.3.2 (Community Edition)
# Build #PC-173.4127.16, built on December 19, 2017
# JRE: 1.8.0_152-release-1024-b8 amd64
# JVM: OpenJDK 64-Bit Server VM by JetBrains s.r.o
# Windows 10 10.0
# Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) 
# [MSC v.1900 64 bit (AMD64)] on win32


# 列表是有一系列特定顺序排列的元素组成的，
# 可以把字符串、数字、字典等任何对象加入到列表中，
# 其中的元素之间没有任何关系，列表也是自带下标的，默认从0开始

l = [1,2,3.1415926,'a','b','c',True,{"name":"zyy"}]
print(l)
# [1, 2, 3.1415926, 'a', 'b', 'c', True, {'name': 'zyy'}]

# 字典有哪些常用方法呢

l.append("hello")
print(l)
# [1, 2, 3.1415926, 'a', 'b', 'c', True, {'name': 'zyy'}, 'hello']

# pop 删除元素 ,默认删除最后一个元素
l.pop()
print(l)
# [1, 2, 3.1415926, 'a', 'b', 'c', True, {'name': 'zyy'}]
l.pop(2)         # 删除下标为2的元素
print(l)
# [1, 2, 'a', 'b', 'c', True, {'name': 'zyy'}]

# remove 删除元素,直接删除元素，remove(value)

# index(value) 查找元素对应的下标
print(l.index("a"))
# 2


m = [1,34,234,54,543,5,533,4,5432]
print(m)
# [1, 34, 234, 54, 543, 5, 533, 4, 5432]
m.sort()
print(m)
# [1, 4, 5, 34, 54, 234, 533, 543, 5432]
m.reverse()
print(m)
# [5432, 543, 533, 234, 54, 34, 5, 4, 1]

# insert  插入新的元素     insert(index, value)
m.insert(3,"hello")
print(m)


