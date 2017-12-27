#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      : 2017/12/3 20:18
# @Author    : zhouyuyao
# @File      : eight.py

# 题目：输出 9*9 乘法口诀表。
# 程序分析：分行与列考虑，共9行9列，i控制行，j控制列。


for i in range(1, 10):
    for j in range(1, i + 1):
        print("%d*%d=%d" % (i, j, i * j),)

