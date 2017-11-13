#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time      :2017/11/3 8:24
#@Author    :zhouyuyao
#@File      :highFunc.py

# map()函数，第一个参数为自定义函数，第二个参数为一个可迭代对象
from functools import reduce

# lt=(1,2,3,4,5)
# def f2(x):
#     return x*x
# ml=map(f2,lt)
# print(type(ml))
# print(list(ml))    # map 函数要想得到列表 得用 list() 转换 否则得到的是 map 对象

# reduce 函数
# 传入的函数必须接受两个参数：
# 把可迭代对象的前两个参数作为参数的实参，传入到 f 函数中
# 把每次 f 运算的结果作为第一个实参，可迭代对象的下一个元素作为另一个实参，传入函数 f 中，
# 以此类推，最终得到结果
# def f(x,y):
#     return x+y
# print(reduce(f,[1,2,3,4,5,],10))   # reduce 函数需引入包
# # from functools import reduce


# filter 函数
# 每次把可迭代对象的元素传入进去，如果返回为 True ，则保留该元素，如果返回False，则不保留
a=[1,2,3,4,5]
def is_odd(x):
    return x%2==1
b=list(filter(is_odd,a))
print(b)
# 此处应该将 filter 函数转换成 list，否则得到的是 filter 对象



