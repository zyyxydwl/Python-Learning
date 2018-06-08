#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/5/18 17:57
# @Author  : zhouyuyao
# @File    : demon3.py
import redis
import time

pool = redis.ConnectionPool(host='120.76.214.30', port=11111, decode_responses=True)
r = redis.Redis(connection_pool=pool)

# pipe = r.pipeline(transaction=False)    # 默认的情况下，管道里执行的命令可以保证执行的原子性，执行pipe = r.pipeline(transaction=False)可以禁用这一特性。
# pipe = r.pipeline(transaction=True)
pipe = r.pipeline() # 创建一个管道

pipe.set('name', 'jack')
pipe.set('age', '22')
pipe.sadd('exes', 'female')
pipe.incr('num')    # 如果num不存在则vaule为1，如果存在，则value自增1
pipe.execute()

print(r.get("name"))
print(r.get("age"))
print(r.get("sex"))
