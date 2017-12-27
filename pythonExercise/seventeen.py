#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      : 2017/12/12 22:24
# @Author    : zhouyuyao
# @File      : seventeen.py

# 题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
# 程序分析：利用while语句,条件为输入的字符不为'\n'。

import string
s= input("Please input a string number :")
letters=0
space=0
digit=0
others=0

for c in s:
    if c.isalpha():         # 检测字符串是否只由字母组成
        letters+=1
    elif c.isspace():       # 检测字符串是否只由空格组成
        space+=1
    elif c.isdigit():       # 检测字符串是否只由数字组成
        digit+=1
    else:
        others+=1
print("char = %d,space = %d,digit = %d,others = %d" % (letters,space,digit,others))

