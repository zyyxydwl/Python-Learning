#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :2017/10/18 14:42
# @Author    :zhouyuyao
# @File      :first.py



#strip
b=' ewui rqh fui rfe '
print(b)
print(b.strip())
print(b.rstrip())
print(b.lstrip())

#format 提高执行效率
name='zhouyuyao'
age=21
print('hello ' + name)
print('hello %s',name)
# %s 表示字符串，%d 表示整型， %f表示浮点型
print("hello {0}".format(name))      #执行效率是最高的
print("Hello {0},your age is: {1}".format(name,age))


