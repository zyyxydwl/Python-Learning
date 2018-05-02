#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/4/22 23:35
# @Author  : zhouyuyao
# @File    : demon3.py
# PyCharm 2017.3.2 (Community Edition)
# Build #PC-173.4127.16, built on December 19, 2017
# JRE: 1.8.0_152-release-1024-b8 amd64
# JVM: OpenJDK 64-Bit Server VM by JetBrains s.r.o
# Windows 10 10.0
# Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) 
# [MSC v.1900 64 bit (AMD64)] on win32


class People(object):
    # 定义基本属性
    color = 'yellow'

    # 定义私有属性,私有属性在类外部无法直接进行访问
    __age = '21'

    def think(self):
        self.color = "black"
        print("I'm a {}.".format(self.color))
        print("I'm a thinker.")

    # 定义构造方法
    def __init__(self,c,a):
        self.color = c
        self.__age = a

jack = People('blue','22')
jack.think()
