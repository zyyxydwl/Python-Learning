#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/5/25 23:25
# @Author  : zhouyuyao
# @File    : demon2.py
# tasks.py
import time
from celery import Celery
from celery.schedules import crontab

app = Celery('tasks', broker='redis://120.76.214.30:11111/0')


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    sender.add_periodic_task(10.0, test.s('hello'), name='add every 10')

    # Calls test('world') every 30 seconds
    sender.add_periodic_task(30.0, test.s('world'), expires=10)

    # Executes every Monday morning at 7:30 a.m.
    sender.add_periodic_task(
        crontab(hour=7, minute=30, day_of_week=1),
        test.s('Happy Mondays!'),
    )


@app.task
def test(arg):
    print(arg)
