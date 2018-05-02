#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/5/1 16:52
# @Author  : zhouyuyao
# @File    : demon7.py
import re

print(re.split('\w+', 'zhouyuyao, zhouyuyao, zhouyuyao.'))
# \w  小写w，匹配数字、字母、下划线
# 结果 ['', ', ', ', ', '.']

print(re.split('(\W+)', ' zhouyuyao, zhouyuyao, zhouyuyao.'))
# \W  大写W，匹配非数字、字母、下划线
# 结果 ['', ' ', 'zhouyuyao', ', ', 'zhouyuyao', ', ', 'zhouyuyao', '.', '']

print(re.split('\W+', ' zhouyuyao, zhouyuyao, zhouyuyao.', 1))
# 结果 ['', 'zhouyuyao, zhouyuyao, zhouyuyao.']

print(re.split('a.*', 'hello world'))  # 对于一个找不到匹配的字符串而言，split 不会对其作出分割
# 结果 ['hello world']

