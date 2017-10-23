#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time      :2017/10/23 20:33
#@Author    :zhouyuyao
#@File      :third.py


strl='werwfrwefrvrtgrg'
print(type(strl))
print(list(strl))

a=['a','b','c','abc','n']
print(a)
print(type(a))
#print(dir(a))

#append 追加
a.append('hello')
print(a)

#index 和str的find差不多
print(a[0],a[2])
print(a.index('abc'))

#insert 在0位置上插入zhouyuyao
a.insert(0,'zhouyuyao')
print(a)
a.insert(3,'zyy3')     #在3位置上插入zyy3
print(a)

#remove 删除,只删除一个元素，删多个写多个
print('remove' * 3)
print(a)
a.insert(3,'abc')
print(a)
a.remove('abc')
a.remove('abc')
print(a)

#sort 排序
print('sort ' * 3)
print(a)
a.sort()   #这个排序存在字符串和数字的原因是会出现错误异常退出的
print(a)

b=['e','d','c','a','b']   #当列表都是字符串时，则可以进行排序
b.sort()
print(b)

#reverse 反序
print(a)
a.reverse()
print(a)

#切片
print(a[3:])
print(a[1:5])
#注意：切片时，取得是最后一位-1，（1:5代表的是原列表中的位置）
