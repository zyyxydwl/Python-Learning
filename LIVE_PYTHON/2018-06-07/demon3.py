#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/6/8 10:12
# @Author  : zhouyuyao
# @File    : demon2.py

import csv

# 使用数字和字符串的数字都可以
datas = [
    {'姓名': '张沐青', '性别': '女', '民族': '汉族', '专业名称': '金融管理', '成绩': '62'}
]

filename = "E:/GitHub/Python-Learning/LIVE_PYTHON/2018-06-05/学位英语成绩合格汇总表.csv"

with open(filename, "a") as f:
    headers = [k for k in datas[0]]        # 取出待写入数据中的 key 值
    writer = csv.DictWriter(f, headers)
    writer.writeheader()
    for row in datas:
        writer.writerow(row)
    # 写入多行
    # writer.writerows(datas)

with open(filename, 'r+') as csv_file:
    reader = csv.DictReader(csv_file)
    print(str([row for row in reader]),end="")
