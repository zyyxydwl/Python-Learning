#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time      :2017/10/25 22:49
#@Author    :zhouyuyao
#@File      :nineth.py

for i in range(10):
    if i>3:
        break
    print('a=' +str(i))

print('#' *20)

i=0
for i in range(1,5):
    print(i)
    if i==3:
        print('hello world')
        continue
    print('i = %d' %i)

