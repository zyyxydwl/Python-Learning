#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/6/8 10:49
# @Author  : zhouyuyao
# @File    : demon4.py
import csv


filename = 'E:/GitHub/Python-Learning/LIVE_PYTHON/2018-06-05/学位英语成绩合格汇总表.csv'
with open(filename) as f:
    reader = csv.DictReader(f)
    for row in reader:
        # Max TemperatureF 是表第一行的某个数据，作为key
        max_temp = row['Max TemperatureF']
        print(max_temp)