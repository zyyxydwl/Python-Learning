#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/6/8 10:12
# @Author  : zhouyuyao
# @File    : demon2.py

import csv

# 使用数字和字符串的数字都可以
datas=[
    ['朱丽蓉', '女', '汉族', '金融管理', '84'],
    ['吴江滔', '女', '汉族', '企业财务管理', '78']
]

filename = "E:/GitHub/Python-Learning/LIVE_PYTHON/2018-06-05/学位英语成绩合格汇总表.csv"
with open(filename,"a",newline="") as f:
    writer = csv.writer(f)
    for row in datas:
        writer.writerow(row)

    # 写入多行
    writer.writerows(datas)


