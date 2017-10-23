#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time      :2017/10/23 21:17
#@Author    :zhouyuyao
#@File      :fourth.py

str1='wequfiiwrfew'
print(tuple(str1))
print(type(tuple(str1)))

a=('a','e','c',342)
print(a)

# tuple 需要注意的是:单个tuple值的时候需要在最后加','。
m=('a')
print(type(m))   #字符串str类型
#返回结果: <class 'str'>

n=('abc',)
print(type(n))   #元祖类型
#返回结果: <class 'tuple'>

#查看tuple的方法: count, index
print(dir(n))

tul=('a','b','b','e','b')
#count 统计某个元素的个数
print(tul.count('b'))

#index 返回某个元素的下标
print(tul.index('e'))

