#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      : 2018/1/1 17:55
# @Author    : zhouyuyao
# @File      : eatPeach.py


# 2. 猴子吃桃问题：猴子第一天摘下若干个桃子,当即吃了一半,
# 还不瘾,又多吃了一个，第二天早上又将剩下的桃子吃掉一半,又多吃了一个。
# 以后每天早上都吃了前一天剩下的一半零一个。
# 到第10天早上想再吃时,见只剩下一个桃子了。求第一天共摘了多少。
# 程序分析：采取逆向思维的方法,从后往前推断。

n=1    #'''定义第9天有n个桃'''
for day in range(0,9):       #range(1,9)表示桃子吃了9天
    n=2*(n+1)                #n=2n+1+1前一天的桃子数
print(n)

# x = 1
# for day in range(0,9):
#     x = (x+1)*2
# print(x)

day1 = 10      #开始有10天
peachNumber = 1   #桃子个数
while day1 > 1:    #天数大于1的时候进行计算
    day1 -= 1      #前一天
    peachNumber = (peachNumber+1)*2   #前一天的桃子个数
    print("day {0} peach {1}".format(day1,peachNumber) )

# x2 = 1
# for day in range(9,0,-1):
#     x1 = (x2 + 1) * 2
#     x2 = x1
