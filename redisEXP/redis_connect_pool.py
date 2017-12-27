#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :2017/11/26 23:10
# @Author    :zhouyuyao
# @File      :redis_connect_pool.py


import redis

redis_config = {
    "host": "47.52.159.109",
    "port": "6379"
}

r = redis.Redis(**redis_config)
r.set("zhouyuyao", "you are beautiful")
print(r.keys())
print(r.get("zhouyuyao"))


pool = redis.ConnectionPool(host="192.168.48.128")
r = redis.Redis(connection_pool=pool)
r.set("zhouyuyao", "you are beautiful")
print(r.keys())
print(r.get("zhouyuyao"))
