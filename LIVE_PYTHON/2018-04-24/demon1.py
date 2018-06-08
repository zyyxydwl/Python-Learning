#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/5/29 10:25
# @Author  : zhouyuyao
# @File    : demon1.py
from datetime import datetime
print(datetime.now())                          #获取当前时间
print(datetime.now().year)                     #年
print(datetime.now().month)                    #月
print(datetime.now().day)                      #日
print(datetime.now().hour)                     #时
print(datetime.now().minute)                   #分
print(datetime.now().second)                   #秒
print(datetime.now().strftime("%Y-%m-%d %I:%M:%S"))     #转换格式为XXXX年-XX月-XX日

''' result:
2018-05-29 10:27:04.248308
2018
5
29
10
27
4
2018-05-29 10:27:04
'''