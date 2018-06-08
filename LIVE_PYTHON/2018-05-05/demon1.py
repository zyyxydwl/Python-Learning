#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/5/5 20:21
# @Author  : zhouyuyao
# @File    : demon1.py
import re

s = "<html>hello world</html>"
reg = re.compile(r"<(?P<tag>\w)>(.*?)</(?P=tag)>")

result = reg.findall(s)
print(result)

