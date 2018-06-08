#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/5/15 20:39
# @Author  : zhouyuyao
# @File    : demon1.py

'''

1、nosql 原理
2、zokeeper 部署，一定是单个，投票的机制 n/2+1，
以集群进行部署的，存储的数据以节点的形式存在的
3、redis 的哨兵
4、keepalived 解决高可用的问题
5、nosql 简介
    类型：字符串、列表、set、hash
6、Python数据类型，set 和 list 的区别
7、set 是不可重复的 list，tuple 是不可更改的 list
8、Python操作redis

'''

import redis   # 导入redis模块，通过python操作redis 也可以直接在redis主机的服务端操作缓存数据库

r = redis.Redis(host="120.76.214.30", port=11111, decode_responses=True)   # host是redis主机，需要redis服务端和客户端都启动 redis默认端口是6379
r.set("name", "zhouyuyao")  # key是"name" value是"zhouyuyao" 将键值对存入redis缓存
print(r["name"])
print(r.get("name"))  # 取出键name对应的值
print(type(r.get("name")))
