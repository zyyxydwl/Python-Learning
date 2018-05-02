#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

line = "You have never giveup"

Obj = re.match(r'(.*) have (.*?) .*', line, re.M | re.I)
# re.M     多行匹配，影响 ^ 和 $
# re.I     使匹配对大小写不敏感

if Obj:
    print("Obj.group() : ", Obj.group())
    print("Obj.group(1) : ", Obj.group(1))
    print("Obj.group(2) : ", Obj.group(2))
else:
    print("No Obj!")
