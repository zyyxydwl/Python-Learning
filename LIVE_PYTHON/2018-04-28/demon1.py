#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

# # 在起始位置匹配，只返回一个结果
# print(re.match('www', 'www.zhouyuyao.cn'))
#
# # 在起始位置匹配，过滤掉一些信息，只留位置，返回元组
# print(re.match('www', 'www.zhouyuyao.cn').span())
#
# # 在起始位置匹配，返回字符串
# print(re.match('www', 'www.zhouyuyao.cn').group(0))
#
# # 不在起始位置匹配
# print(re.match('cn', 'www.zhouyuyao.cn'))

# 在起始位置匹配，只返回一个结果
print(re.search('www', 'www.zhouyuyao.cn'))
# 结果 <_sre.SRE_Match object; span=(0, 3), match='www'>

# 在起始位置匹配，span 过滤掉一些信息，只留位置，返回元组
print(re.search('www', 'www.zhouyuyao.cn').span())
# 结果 (0, 3)

# 在起始位置匹配，返回字符串
print(re.search('www', 'www.zhouyuyao.cn').group(0))
# 结果 www

# 不在起始位置匹配
print(re.search('cn', 'www.zhouyuyao.cn'))
# 结果 <_sre.SRE_Match object; span=(14, 16), match='cn'>

# 不在起始位置匹配，span 过滤掉一些信息，只留位置，返回元组
print(re.search('cn', 'www.zhouyuyao.cn').span())
# 结果 (14, 16)

