#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/4/13 9:54
# @Author  : zhouyuyao
# @File    : repFile.py
# PyCharm 2017.3.2 (Community Edition)
# Build #PC-173.4127.16, built on December 19, 2017
# JRE: 1.8.0_152-release-1024-b8 amd64
# JVM: OpenJDK 64-Bit Server VM by JetBrains s.r.o
# Windows 10 10.0
# Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) 
# [MSC v.1900 64 bit (AMD64)] on win32

# 语法
# walk()方法语法格式如下：
# os.walk(top[, topdown=True[, onerror=None[, followlinks=False]]])
# 参数
# top -- 是你所要便利的目录的地址, 返回的是一个三元组(root,dirs,files)。
# root 所指的是当前正在遍历的这个文件夹的本身的地址
# dirs 是一个 list ，内容是该文件夹中所有的目录的名字(不包括子目录)
# files 同样是 list , 内容是该文件夹中所有的文件(不包括子目录)
# topdown --可选，为 True，则优先遍历 top 目录，否则优先遍历 top 的子目录(默认为开启)。如果 topdown 参数为 True，walk 会遍历top文件夹，与top 文件夹中每一个子目录。
# onerror -- 可选， 需要一个 callable 对象，当 walk 需要异常时，会调用。
# followlinks -- 可选， 如果为 True，则会遍历目录下的快捷方式(linux 下是 symbolic link)实际所指的目录(默认关闭)。

import os
def get_files():
    for dirpath, dirs, files in os.walk(r"E:\wxorder", topdown=False):
        for name in files:
            print(os.path.join(dirpath, name))
            # print(os.path.join(name))
        # for name in dirs:
        #     print(os.path.join(dirpath, name))
get_files()



# #方法4：非递归
# import os
#
# for dirpath, dirnames, filenames in os.walk('E:\wxorder'):
#     print(dirpath, dirpath)
#     for filename in filenames:
#         print(dirpath, filename)



