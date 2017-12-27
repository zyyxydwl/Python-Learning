#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      : 2017/12/24 16:24
# @Author    : zhouyuyao
# @File      : two.py

# 现有列表
# list1 = ['XXXX', 'b', 3, 'c', '&', 'a', 3, '3', 3, 'aa', '3', 'XXXX']
# list2 = ['e', 'f', 'g']
list1 = ['XXXX', 'b', 3, 'c',3, '&', 'a', 3, '3', 3, 'aa', '3', 'XXXX']
list2 = ['e', 'f', 'g']

# 要求对其做以下操作：
# 1. 取出 ‘XXXX’ 中间的部分，形成一个新的列表list3
list3=list1[1:-1]
print(list3)

# 2. 对list3 做一下几部操作
# 1）删除特殊符号
# list3.remove(list3[3])
del list3[4]
print(list3)

# 2）统计 3 在list3中出现的次数
print(list3.count(3))

# 3）用最简短的代码去除list3中 26个字母以外的元素(要求只能对list3操作)
# ['b', 3, 'c', 'a', 3, '3', 3, 'aa', '3']
# ['b', 3, 'c', 3, 'a', 3, '3', 3, 'aa', '3']
list3=list3[0:5:2]
print(list3)

# 4）对list3排序
list3.sort()
print(list3)

# 5）在末尾追加'd',并把list2追加到list3
list3.append('d')        # 在末尾追加'd'，append可以追加字符串或元组
print(list3)
list3.extend(list2)      # 把list2追加到list3中，extend值能追加一个列表
print(list3)

# 3. 现有两个变量
# a = ('h',)
# b = ('h')
a = ('h',)
b = ('h')
# 1）将a和b分别追加到上一题的list3中，观察有什么区别
list3.extend(a)
print(list3)
list3.extend(b)
print(list3)

# 2）将1生成的list3转换成元组(扩展：自己搜索方法)
print(tuple(list3))

# 3）打印出只有一个元素'h'的元组，在2中生成的元组中的索引
list4=('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'h')
print(list4.index(a))





