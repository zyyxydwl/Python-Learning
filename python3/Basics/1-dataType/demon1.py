#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/1/21 17:15
# @Author  : zhouyuyao
# @File    : demon1.py
# PyCharm 2017.3.2 (Community Edition)
# Build #PC-173.4127.16, built on December 19, 2017
# JRE: 1.8.0_152-release-1024-b8 amd64
# JVM: OpenJDK 64-Bit Server VM by JetBrains s.r.o
# Windows 10 10.0
# Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) 
# [MSC v.1900 64 bit (AMD64)] on win32

# 整型 int
a=10
print(a)
# print a      python2支持

# bool      True     False
# >=1       True
# <=0       False

# float 浮点值
a=3.141592653
m = round(a,2)           # 保留两位小数
print(m)
# round(float,ndigits)
# float代表数字，ndigits代表精度
# 大的规则是四舍五入

# 字符串 str  'abc'   "abc"    '''abc'''
string = 'abcadefgahiagh'
print(string)


# find  查找字符串，如果找到就返回字符串开始的下标，如果没有找到则返回-1
print(string[0])        # 打印下标为0的值
print(string[3])        # 打印下标为3的值
print(string[:])        # 打印所有值
result = string.find('def')
print(result)
# 3   返回下标3

# replace 替换
print(string.replace("a","AAA"))

# split   分隔符
# join(可迭代对象)    一般为list字符串
newlist = string.strip().split("a")
print(newlist)
print("   ###   ".strip().join(newlist))



# strip()  去除字符串前后的空字符
string.strip()

# print("My string is : %s" % string)
print("My string is : {0}".format(string))  # 推荐使用,效率最高

print("hello" + "world")


















