#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time      :2017/10/28 9:13
#@Author    :zhouyuyao
#@File      :file_with.py
import codecs


f = open('test.txt','r')
f.close()

with codecs.open('test.txt','r') as f:
# 使用 with 无需在最后 close 关闭文件，读完后直接关闭
    print(f.read())
    print(f.closed)
print(f.closed)   # 打印文件是否关闭 True or False

with codecs.open('test.txt','r') as f1:
    for line,vlaue in enumerate(f1):
        print(line,vlaue)

import linecache
count=linecache.getline('test.txt',4)   # 打印文件的第四行
print(count)
