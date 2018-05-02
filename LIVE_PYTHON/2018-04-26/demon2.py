#!/usr/bin/env python
# -*- coding:utf-8 -*-



# from io import StringIO
#
# f = StringIO()
# f.write('have ')
# f.write('a')
# f.write(' ')
# f.write('nice ')
# f.write('day')
# print(f.getvalue())      # getvalue()方法用于获得写入后的str


from io import StringIO
f = StringIO('Hello a good day!')
print(type(f))         # <class '_io.StringIO'>
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())


# 运行结果
# <class '_io.StringIO'>
# Hello a good day!
# 运行结果