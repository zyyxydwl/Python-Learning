#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/4/22 23:04
# @Author  : zhouyuyao
# @File    : demon1.py
# PyCharm 2017.3.2 (Community Edition)
# Build #PC-173.4127.16, built on December 19, 2017
# JRE: 1.8.0_152-release-1024-b8 amd64
# JVM: OpenJDK 64-Bit Server VM by JetBrains s.r.o
# Windows 10 10.0
# Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) 
# [MSC v.1900 64 bit (AMD64)] on win32

class ren(object):
    '''this class is about ren class。类的说明，使用三个单引号'''
    name='菇凉'
    sex='Female'
    def hello(self):
        # print('hello world')       # 如使用 print,在后面调用方法时会显示 None
        return 'hello world'

# 实例化类
a=ren()
print(type(a))

# 访问类的属性和方法
print('ren 类的属性 name 为: {0}'.format(a.name))     # 输出类的属性 name
print('ren 类的属性 sex 为: {0}'.format(a.sex))      # 输出类的属性 sex
print('ren 类的方法 hello 输出为: {0}'.format(a.hello()))
# a.name='未来啊'
# print(a.name)
