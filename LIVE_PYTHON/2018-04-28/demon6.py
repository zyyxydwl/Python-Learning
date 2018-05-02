#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/5/1 16:45
# @Author  : zhouyuyao
# @File    : demon6.py
# import re
#
# pattern = re.compile(r'\d+')  # 查找数字,匹配1个或多个的数字
# result1 = pattern.findall('zyy 123 google 456')
# result2 = pattern.findall('z88hou123yuyao456', 0, 10)
#
# print(result1)
# print(result2)

import re

it = re.finditer(r"\d+", "12a32bc43jf3")
for match in it:
    print(match.group())