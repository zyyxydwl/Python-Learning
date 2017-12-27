#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      : 2017/12/13 23:13
# @Author    : zhouyuyao
# @File      : eighteen.py

# 题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。
# 例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
# 程序分析：关键是计算出每一项的值。
from functools import reduce

sum=0
Ssum=[]
n=int(input("n = "))
q=int(input("q = "))
for count in range(n):
    sum+=n
    q=q*10
    Ssum.append(sum)
    print(Ssum)

Ssum=reduce(lambda x,y :x+y,Ssum)
print("The sum is : {0}".format(Ssum))

