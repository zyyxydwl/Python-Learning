#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/5/27 23:13
# @Author  : zhouyuyao
# @File    : celery-config.py
from kombu import Queue, Exchange

BROKER_URL = "redis://120.76.214.30:11111/0"
CELERY_RESULT_BACKEND = "redis://120.76.214.30:11112/0"

CELERY_QUEUES = {
    Queue("default",Exchange("default"),routing_key="default"),
    Queue("for_task_A",Exchange("for_task_A"),routing_key="for_task_A"),
    Queue("for_task_B",Exchange("for_task_B"),routing_key="for_task_B")
}

CELERY_ROUTES = {
    "demon1.taskA":{"queue":"for_task_A","routing_key":"for_task_A"},
    "demon1.taskB":{"queue":"for_task_B","routing_key":"for_task_B"}
}
CELERY_TIMEZONE = 'UTC'
CELERYBEAT_SCHEDULE = {
    'taskA_schedule' : {
        'task':'demon1.taskA',
        'schedule':2,
        'args':(5,6)
    },
    'taskB_scheduler' : {
        'task':"demon1.taskB",
        "schedule":10,
        "args":(10,20,30)
    },
    'add_schedule': {
        "task":"demon1.add",
        "schedule":5,
        "args":(1,2)
    }
}