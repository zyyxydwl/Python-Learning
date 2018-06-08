#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/5/29 15:24
# @Author  : zhouyuyao
# @File    : demon3.py
import random
import string




# 随机打印6位验证码
print("".join(random.sample(string.ascii_letters + string.digits, 14)))
