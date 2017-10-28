#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time      :2017/10/27 22:31
#@Author    :zhouyuyao
#@File      :file_gena1.py
import codecs
# readlines() 方法，读取文件所有内容
# 是把文件中每行的内容作为一个字符串中的单个元素
# 放在一个列表 list 中
f=codecs.open('w2.txt')
#print(dir(f))
text=f.readlines()
#print(f.readlines())
print(text)
print(type(text))
f.close()


# readline() 读取文件一行内容
# __next__() 读取文件下一行内容
f=codecs.open('w2.txt','r')
print(f.readline())
print(f.__next__())
f.close()


# write() 必须传入字符串
# writelines() 必须传入一个序列 list

f=open('w3.txt','w')
f.write('hello world\n dhwuirhfwirfewfrf\n')
f.close()


