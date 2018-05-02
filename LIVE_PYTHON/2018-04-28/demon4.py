#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/5/1 15:36
# @Author  : zhouyuyao
# @File    : demon4.py


import re

phone = "0731-2734-538 # 这是一个电话号码"

# 第一种 删除注释
num = re.sub(r'#.*$', "", phone)
# .	    匹配任意字符，除了换行符，当re.DOTALL标记被指定时，则可以匹配包括换行符的任意字符
# $	    匹配字符串的末尾。
# re*	匹配0个或多个的表达式
print("去掉#号后面的字符串的电话号码为 : ", num)
# 结果 去掉#号后面的字符串的电话号码为 :  0731-2734-538


# 第二种 移除非数字的内容
num = re.sub(r'\D',"", phone)
# num = re.sub(r'\D',"", phone)
# \D    匹配任意非数字
print("移除非数字的内容后的电话号码 : ",num)
# 结果 移除非数字的内容后的电话号码 :  07312734538

