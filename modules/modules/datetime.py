#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time      :2017/11/9 21:21
#@Author    :zhouyuyao
#@File      :datetime.py

# Subclass relationships: 这类直接的对应关系

# object
# timedate
# tzinfo
# time       #基本不使用
# date
# datetime    #一般使用 datetime 取时间
import time
for i in range(1,10):
    print(i)
    time.sleep(0.1)

# datetime

from _datetime import datetime
# print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))   # 格式化输出时间
# a=datetime.now().strftime('%c')
# print(a)
# # now 获得当前时间，strftime用来显示格式化的时间
#
# now_time=datetime.now()
# print(now_time)
# print(type(now_time))       # <class 'datetime.datetime'>
#
# _time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# print(type(_time))          # <class 'str'>
# _d_time=datetime.now().strptime(_time, '%Y-%m-%d %H:%M:%S')
# print(type(_d_time))        # <class 'datetime.datetime'>


# 时间戳 time stamp
_a=time.time()
print(_a)                     # 1510242881.532264
_m_time=datetime.fromtimestamp(_a)
print(_m_time)                # 2017-11-09 23:54:41.532264
print(type(_m_time))          # <class 'datetime.datetime'>


