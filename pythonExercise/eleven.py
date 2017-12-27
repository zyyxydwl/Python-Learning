#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      : 2017/12/4 23:19
# @Author    : zhouyuyao
# @File      : eleven.py

# 题目：判断101-200之间有多少个素数，并输出所有素数。
# 程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数。 　　

import math


def sushu(start, end):
    count = 0
    for i in range(start, end + 1):
        if (i % 2 == 0 and i != 2):  # 去除除2以外的偶数
            continue
        for j in range(2, int(math.sqrt(i)) + 1):
            if (i % j == 0):
                break
        else:
            count = count + 1
            print(i, end=" ")
    print("")
    print("count", count)
    return


# start=int(input("start:\n"))
# end=int(input("end:\n"))
# sushu(start,end)

sushu(101, 200)