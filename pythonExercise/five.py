#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time      :2017/12/3 19:22
#@Author    :zhouyuyao
#@File      :five.py


# 题目：输入三个整数x,y,z，请把这三个数由小到大输出。
# 程序分析：我们想办法把最小的数放到x上，
# 先将x与y进行比较，如果x>y则将x与y的值进行交换，然后再用x与z进行比较，
# 如果x>z则将x与z的值进行交换，这样能使x最小。

l=[]
for i in range(3):
    x=int(input('integer: \n'))       # integer 整数
    l.append(x)  # append() 方法用于在列表末尾添加新的对象。
l.sort()  # 在原位上重新排列列表，未创建新的列表
# 　　1、列表的成员函数：L.sort()，在原位重新排列列表，未创建新的列表；
# 　　2、内建函数：sorted(L)，产生一个新的列表，不改变原列表；
print(l)
