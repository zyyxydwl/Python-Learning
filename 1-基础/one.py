#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      : 2017/12/21 9:02
# @Author    : zhouyuyao
# @File      : one.py

str1=" abcdeFGh &*ijklopqmnrst((uvwxyz"
str2="ABC  # DEF  GH%IJ MNOPQ KLRS&&TUVWX(*&YZ"

a=str1.replace(' ','')
b=a.replace('&','')
c=b.replace('(','')
d=c.replace('*','')
e=d.lower()
# print(e)
demo=["1","4","3","2"]
print(demo.reverse())
# print(d.)

h=str2.replace(' ','')
i=h.replace('#','')
j=i.replace('%','')
k=j.replace('&','')
m=k.replace('*','')
n=m.replace('(','')
l=n.upper()
# print(l)

f=e[::-1]
sumstr=l+f
print(sumstr)
