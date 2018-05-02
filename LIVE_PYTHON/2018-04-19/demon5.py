#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/4/23 0:06
# @Author  : zhouyuyao
# @File    : demon5.py
# PyCharm 2017.3.2 (Community Edition)
# Build #PC-173.4127.16, built on December 19, 2017
# JRE: 1.8.0_152-release-1024-b8 amd64
# JVM: OpenJDK 64-Bit Server VM by JetBrains s.r.o
# Windows 10 10.0
# Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) 
# [MSC v.1900 64 bit (AMD64)] on win32
# 类定义
class People(object):
    # 定义基本属性
    color = 'yellow'
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __age = '21'
    # 定义构造方法
    def __init__(self,n,c):
        self.dwell = 'Earth'
        self.name = n

    def think(self):
        self.color = "black"
        print("I'm a {}.".format(self.color))
        print("My home is on the earth.".format(self.dwell))

# 单继承示例
class Chinese(People):
    grade = ''
    def __init__(self,c,a,g):    # 需添加覆写的属性 g
        # 调用父类的构函
        People.__init__(self,c,a)
        self.grade = g
    # 覆写父类的方法
    def think(self):
        print("I like {0},and I got {1} at last test.".format(self.color,self.grade))

# 另一个类，多重继承之前的准备
class Martian(object):
    color = 'red'
    def __init__(self,y):
        self.habit = y
    def think(self):
        print("I like {0}.".format(self.habit))


# 多重继承
class Sample(Martian,Chinese):
    a=''
    def __init__(self,c,a,g,y):
        Chinese.__init__(self,c,a,g)
        Martian.__init__(self,y)

cn = Sample('zyy',21,100,'yoga')
cn.think()    # 方法名同，默认调用的是在括号中排前地父类的方法
