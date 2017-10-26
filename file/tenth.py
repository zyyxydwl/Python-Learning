#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time      :2017/10/26 21:38
#@Author    :zhouyuyao
#@File      :tenth.py


#实现1-100的和
print(sum(range(1,101)))



#实现1-500所有奇数的和
m=0
for n in range(1,501):
    if n%2 == 1:
        m=n+m
print(m)

print(sum(range(1,501,2)))



#求1+2！+3！+4！+······+20！的和
a=0
b=1
c=0
for a in range(1,21):
    b=b*a
    c=c+b
print(c)



#对一个指定的list进行排序 [2,32,43,453,54,6,576,5,7,6,8,78,7,89]
list=[2,32,43,453,54,6,576,5,7,6,8,78,7,89]
list.sort()
print(list)



