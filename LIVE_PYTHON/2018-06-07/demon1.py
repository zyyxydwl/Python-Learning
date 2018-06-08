#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/6/7 20:43
# @Author  : zhouyuyao
# @File    : demon1.py

'''
1、Python发送邮件附带图片
2、数据处理
excel、pdf
3、爬下来的pdf文件封装成一个PDF文件
'''
import csv

filename = "E:/GitHub/Python-Learning/LIVE_PYTHON/2018-06-05/学位英语成绩合格汇总表.csv"
with open(filename) as f:
    reader = csv.reader(f)
    # 读取一行，下面的reader中已经没有该行了
    # head_row=next(reader)
    for i in reader:
        # 行号从2开始
        print(reader.line_num,i)



