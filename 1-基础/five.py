#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      : 2017/12/27 9:58
# @Author    : zhouyuyao
# @File      : five.py

# 习题
# 1. 有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
# 1.程序分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去掉不满足条件的排列。

from itertools import permutations, count
diffNum=list()
for i in permutations(range(1,5),3):
    '''
    permutations(iterable, r=None):
    permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    permutations(range(3)) --> 012 021 102 120 201 210
    创建一个迭代器，返回iterable中所有长度为r的项目序列，
    如果省略了r，那么序列的长度与iterable中的项目数量相同：
    返回p中任意取r个元素做排列的元组的迭代器
    '''
    diffNum.append(i)
print(len(diffNum))
print(diffNum)


# 2. 打印出所有的“水仙花数”,所谓“水仙花数”是指一个三位数,其各位数字立方和等于该数本身。
# 例如：153是一个“水仙花数”,因为153=1的三次方＋5的三次方＋3的三次方。
# 程序分析：利用for循环控制100-999个数,每个数分解出个位,十位,百位。

for m in range(100,1000):
    i = m % 10             #个位
    v = m / 10 % 10        #十位
    h = m / 10 % 10   #百位
    m =i**3+v**3+h**3
    print(i,v,h)


# 3. 两个乒乓球队进行比赛,各出三人。甲队为a,b,c三人,乙队为x,y,z三人。
# 已抽签决定比赛名单。有人向队员打听比赛的名单。a说他不和x比,c说他不和x,z比,请编程序找出三队赛手的名单。



