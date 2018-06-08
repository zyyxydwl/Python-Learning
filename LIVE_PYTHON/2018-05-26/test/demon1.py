#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/5/27 23:16
# @Author  : zhouyuyao
# @File    : demon1.py
from celery import Celery

app = Celery()                            # 定义了一个Celery的对象
app.config_from_object("celery-config")   # 通过celery-config.py对celery对象进行设置
# 分别定义了三个task
@app.task
def taskA(x, y):
    return x*y

@app.task
def taskB(x, y, z):
    return x+y+z

@app.task
def add(x, y):
    return x+y
