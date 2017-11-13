#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :2017/11/3 9:35
# @Author    :zhouyuyao
# @File      :lambda.py

# 匿名函数：没有名字的函数
def sum(s, y):
    return x * y


m = lambda x, y: x * y
print(m)
print(m(4, 5))

# sorted() 高阶函数
# 对字典进行排序
mm=dict(a=1,c=10,b=4,d=9)
for i in mm:
    print(i)
for j in mm.items():
    print(j)

test=sorted(mm)
print(test)





