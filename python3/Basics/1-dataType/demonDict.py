#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/1/22 23:37
# @Author  : zhouyuyao
# @File    : demonDict.py
# PyCharm 2017.3.2 (Community Edition)
# Build #PC-173.4127.16, built on December 19, 2017
# JRE: 1.8.0_152-release-1024-b8 amd64
# JVM: OpenJDK 64-Bit Server VM by JetBrains s.r.o
# Windows 10 10.0
# Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) 
# [MSC v.1900 64 bit (AMD64)] on win32

# 字典的三种定义方式
d1 = dict(name = "zhou",age = 22)
print(d1)
# {'name': 'zhou', 'age': 22}

d2 = {"id":43245232,"name":"zhoumoumou"}
print(d2)
# {'id': 43245232, 'name': 'zhoumoumou'}

d3 = dict([("ip","1.1.1.1"),("address","ChangSha")])
print(d3)
# {'ip': '1.1.1.1', 'address': 'ChangSha'}


# 方法：
# get(key)        根据key获取value
print(d1.get("name"))
# zhou
print(d1.get("address"))
# None

# setdefault      根据key获取value，如果key不存在，可以设定默认的value
print(d1.setdefault("name"))
# zhou
print(d1.setdefault("address","ChangSha"))
# ChangSha

# 获取所有的keys值
print(d2.keys())
# dict_keys(['id', 'name'])
print(type(d2.keys()))
# <class 'dict_keys'>

# 获取所有的values值
print(d2.values())
# dict_values([43245232, 'zhoumoumou'])
print(type(d2.values()))
# <class 'dict_values'>


for x,y in d3.items():
    print("key = {0},value = {1}".format(x,y))
# key = ip,value = 1.1.1.1
# key = address,value = ChangSha


# update  和list中的 + 类似
# l=list()   l+=[1,2,3,4]
m=dict()
n=dict(name="zhou",age=12)
m.update(n)
print(m)
# {'name': 'zhou', 'age': 12}

# l=list()   l+=[1,2,3,4]
l=list()
m = [1,2,3,4,5,6]
l+=m
print(l)
# [1, 2, 3, 4, 5, 6]


print(d3)
# pop(key)    删除key所对应的元素
keyDelete = d3.pop("ip")
print(keyDelete)
print(d3)



