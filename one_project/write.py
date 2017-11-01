#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time      :2017/10/30 23:29
#@Author    :zhouyuyao
#@File      :sort.py
import codecs

list = ['2','4','3','9','1','7']     # 列表
tul = ('a','b','b','e','b')          # 元组
k={'name':'zhouyuyao','age':21}      # 字典

f=codecs.open('write.txt','w')       # w 表示写
f.write('Hello world\n')             # 将字符串写入文件
f.writelines(str(list)+'\n')         # 将列表写入文件
f.writelines(str(tul)+'\n')          # 将元组写入文件
#f.writelines(tul)          # 将元组写入文件
f.writelines(str(k)+'\n')            # 将字典写入文件
#f.writelines(k)            # 将字典写入文件

