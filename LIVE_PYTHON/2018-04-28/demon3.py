#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/5/1 15:26
# @Author  : zhouyuyao
# @File    : demon3.py

import re

line = "You have never giveup"
# re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None
matchObj = re.match(r'never', line, re.M | re.I)
if matchObj:
    print("match --> matchObj.group() : ", matchObj.group())
else:
    print("No match!!")

# re.search匹配整个字符串，直到找到一个匹配
matchObj = re.search(r'never', line, re.M | re.I)
if matchObj:
    print("search --> matchObj.group() : ", matchObj.group())
else:
    print("No match!!")


