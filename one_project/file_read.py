#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time      :2017/10/27 21:54
#@Author    :zhouyuyao
#@File      :file_demo1.py
import codecs
# 打开文件需要几步：
# 1、open文件
# 2、文件操作（读或者写）
# 3、关闭文件
f=codecs.open('test.txt')
print(f.read())     #相当于把整个文件内容拿出来并当做字符串
print(dir(f))
f.close()

