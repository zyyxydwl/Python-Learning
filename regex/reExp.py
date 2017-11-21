#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time      :2017/11/15 22:26
#@Author    :zhouyuyao
#@File      :reExp.py

# 正则对象的 matche 匹配,较精准的匹配，没找到则返回 NONE

import re
# reg=re.compile(r'abc.*')
# print(type(reg))             # <class '_sre.SRE_Pattern'>
# print(reg)                   # re.compile('abc.*')
# print(dir(reg))              # 查看 reg 的相关方法
reg=re.compile(r'(hello w.*)(hello 1.*)')
a='aahello world hello zhouyuyao'
result=reg.match(a)
print(result)
# None

m = re.match(r"(\d+)\.(\d+)", "24.1632")
print(m.groups())
# ('24', '1632')

b='aa'+a
print(b)
result2=reg.match(b)
print(result2)
# aaaahello world hello zhouyuyao
# None
