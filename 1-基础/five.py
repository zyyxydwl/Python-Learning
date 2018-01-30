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




