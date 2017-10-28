#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time      :2017/10/28 8:38
#@Author    :zhouyuyao
#@File      :file_gena2.py


import codecs

file=codecs.open('gena2.txt','w')
print(dir(file))
file.write('hello world!\nzhouyuyao\n')
print(file.tell())  #打印输入字符的所有个数
file.writelines(['aaaa\n','bbbb\n','cccc\n','dddd'])
print(file.tell())
file.flush()
file.seek(0)
file.write('this teacher is very cool\n')
file.close()

