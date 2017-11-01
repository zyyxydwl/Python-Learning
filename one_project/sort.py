#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time      :2017/10/30 23:29
#@Author    :zhouyuyao
#@File      :sort.py
import codecs

list = ['2','4','3','9','1','7']
list.sort()       # 对 list 进行排序
print(list)       # 打印正序排列的 list

f=codecs.open('sort.txt','w')    # w 表示写
f.writelines(str(list)+'\n')     # 将正序排列的 list 写入 sort.txt 文件,并添加换行符

list.sort(reverse=True)    # 将 list 反序排列
print(list)
f=codecs.open('sort.txt','a')    # a 是追加，将反序排列的了 list 结果追加到文件中
f.write(str(list))
