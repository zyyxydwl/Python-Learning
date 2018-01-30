#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      : 2017/12/28 11:40
# @Author    : zhouyuyao
# @File      : numberRiddle.py

# 接着我们写一个猜数字游戏的小程序，要求如下：
# 1、系统生成一个20以内的随机整数
# 2、玩家有6次机会进行猜猜看，每次猜测都有反馈（猜的数字太大，猜的数字太小，猜对了-结束）
# 3、6次中，猜对了，显示玩家赢了
# 4、否则系统赢了
import random
import sys

intN=random.randint(1,20)
number=input("Please input a number : ")

i=0
while (intN!=number and i<7):
    if int(number) > intN:
        print("You number is too big.")
        continue
    elif int(number) < intN:
        print("You number is too small.")
        continue
    else:
        print("You number is correct.You won it.")
        sys.exit()




