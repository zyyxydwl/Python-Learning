#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/4/22 23:22
# @Author  : zhouyuyao
# @File    : demon2.py
# PyCharm 2017.3.2 (Community Edition)
# Build #PC-173.4127.16, built on December 19, 2017
# JRE: 1.8.0_152-release-1024-b8 amd64
# JVM: OpenJDK 64-Bit Server VM by JetBrains s.r.o
# Windows 10 10.0
# Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) 
# [MSC v.1900 64 bit (AMD64)] on win32
class ren():
    '''this class is about ren class。类的说明，使用三个单引号'''
    def __init__(self,name,sex):        # 构造器
        # 注意到 __init__ 方法的第一个参数永远是 self ，表示创建的实例本身
        # 因此，在 __init__ 方法内部，就可以把各种属性绑定到 self
        # 因为self 就指向创建的实例本身
        # 有了 __init__ 方法，在创建实例的时候，就不能传入空的参数了
        # 必须传入与 __init__ 方法匹配的参数，
        # 但 self 不需要传，python解释器会把实例变量传进去
        self.name=name
        self.sex=sex
    def hello(self):
        print('hello {0}'.format(self.name))   # 调用类的属性

test=ren('zhouyuyao','F')     # 需输入参数
test.hello()

