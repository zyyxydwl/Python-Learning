#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time      :2017/10/23 21:42
#@Author    :zhouyuyao
#@File      :fifth.py



k={'name':'zhouyuyao','age':21,'sex':'female'}
print(k)
print(type(k))
# 返回结果:
# {'name': 'zhouyuyao', 'age': 21, 'sex': 'female'}
# <class 'dict'>

k1=dict(a=1,b=2,c=3)
print(k1)
# 返回结果:
# {'a': 1, 'b': 2, 'c': 3}

# 元组里面一个列表，列表里面两个元组
d=dict([('name','list'),('age',20)])
print(d)
# 返回结果:
# {'name': 'list', 'age': 20}

# 字典的常用方法
k1.clear()    # clear 相当于把 k1 里面的值清除
print(k1)

# get方法
print(k.get('name'))
print(k.get('age'))
# 返回结果:
# zhouyuyao
# 21

# setdefault
print(k.setdefault('name'))
print(k.setdefault('age','changsha'))
print(k.setdefault('address','changsha'))
# 返回结果:
# zhouyuyao
# 21
# changsha

# keys
print(k.keys())
# 返回结果:
# dict_keys(['name', 'age', 'sex', 'address'])

# values
print(k.values())

# iteritems
print(k.items())    #在 python3 里面用 items() 替换 iteritems()
# 返回结果:
# dict_items([('name', 'zhouyuyao'), ('age', 21), ('sex', 'female'), ('address', 'changsha')])


for x,y in k.items():
    print(x,y)
# 返回结果:
# name zhouyuyao
# age 21
# sex female
# address changsha

# Python 3.0 内的另一个重大改变是字典内dict.iterkeys(),dict.itervalues(),dict.iteritems()方法的删除。
# 取而代之的是:dict.keys(),dict.values(),dict.items()，
# 它们被进行了修补，可以返回轻量的、类似于集的容器对象，而不是键和值的列表。
# 这样的好处是在不进行键和条目复制的情况下，就能在其上执行set操作。
# dict.has_key()同样被移除。

l=['a','b','c','d']
m={}
n=m.fromkeys(l,123)
n=dict.fromkeys(l,123)
print(n)
# 返回结果:
# {'a': 123, 'b': 123, 'c': 123, 'd': 123}

l1=['a','b','c','d']
l2=[1,2,3,4]
dict_test=dict(zip(l1,l2))    #应该为字典
print(dict_test)
print(k)
# 返回结果:
# {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# {'name': 'zhouyuyao', 'age': 21, 'sex': 'female', 'address': 'changsha'}

# 将 dict_test 和 k 合并
dict_test.update(k)
print(dict_test)
# 返回结果:
# {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'name': 'zhouyuyao', 'age': 21, 'sex': 'female', 'address': 'changsha'}

# 对字典进行排序
mm=dict(a=1,b=10,c=3,d=9)
print(mm)
print(sorted(mm.items(),key=lambda d: d[1],reverse=True))
# 返回结果:
# {'a': 1, 'b': 10, 'c': 3, 'd': 9}
# [('b', 10), ('d', 9), ('c', 3), ('a', 1)]
