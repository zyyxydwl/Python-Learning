#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/1/29 23:36
# @Author  : zhouyuyao
# @File    : demonDecorator.py
# PyCharm 2017.3.2 (Community Edition)
# Build #PC-173.4127.16, built on December 19, 2017
# JRE: 1.8.0_152-release-1024-b8 amd64
# JVM: OpenJDK 64-Bit Server VM by JetBrains s.r.o
# Windows 10 10.0
# Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) 
# [MSC v.1900 64 bit (AMD64)] on win32


# 装饰器
# 作用：
# 装饰器本质上是一个Python的函数，
# 它可以让其他函数在不需要做任何代码变动的前提下增加额外功能，
# 装饰器的返回值也是一个函数对象。
# 它经常用于在且慢需求的场景，比如：插入日志、性能测试、事务处理、缓存、权限校验等场景。
# 装饰器是解决这类问题的绝佳设计，
# 有了装饰器，我们就可以抽离出大量与函数功能本身无关的雷同代码并继续重用
# 简单来说，就是在不改变函数本身的情况下，在函数的前面或者后面增加一些额外功能

# 原函数
def hello():
    print("hello world")
hello()

# 目的函数
def hello():
    print("###########start###########")
    print("hello world")
    print("############end############")
hello()





