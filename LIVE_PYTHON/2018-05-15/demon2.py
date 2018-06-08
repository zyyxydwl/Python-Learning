#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/5/18 11:35
# @Author  : zhouyuyao
# @File    : demon2.py
import redis    # 导入redis模块，通过python操作redis 也可以直接在redis主机的服务端操作缓存数据库

pool1 = redis.ConnectionPool(host='120.76.214.30', port=11111, decode_responses=True)
pool2 = redis.ConnectionPool(host='120.76.214.30', port=11112, decode_responses=True)

r1 = redis.Redis(connection_pool=pool1)
r2 = redis.Redis(connection_pool=pool2)

# r1.set('gender', 'female')     # key是"gender" value是"male" 将键值对存入redis缓存
# print(r1.get('gender'))      # gender 取出键male对应的值
#
# r2.set('gender', 'male')     # key是"gender" value是"male" 将键值对存入redis缓存
# print(r2.get('gender'))      # gender 取出键male对应的值
# print(r2.keys())
#
# r1.set('food', 'mutton', ex=3)    # key是"food" value是"mutton" 将键值对存入redis缓存
# print(r1.get('food'))  # mutton 取出键food对应的值
#
# r1.set('food', 'beef', px=30)
# print(r1.get('food'))
#
# print(r1.set('fruit', 'watermelon', nx=True))    # True--不存在
# # 如果键fruit不存在，那么输出是True；如果键fruit已经存在，输出是None

# print((r1.set('fruit', 'apple', xx=True)))   # True--已经存在
# 如果键fruit已经存在，那么输出是True；如果键fruit不存在，输出是None

# r1.mget({'k1': 'v1', 'k2': 'v2'})
# r1.mset(k1="v1", k2="v2")           # 这里k1 和k2 不能带引号 一次设置多个键值对
# print(r1.mget("k1", "k2"))          # 一次取出多个键对应的值
# print(r1.mget("k1"))

# print(r1.mget('k1', 'k2'))
# print(r1.mget(['k1', 'k2']))
# print(r1.mget("fruit", "fruit1", "fruit2", "k1", "k2"))  # 将目前redis缓存中的键对应的值批量取出来


# print(r1.getset("fruit", "barbecue"))  # 设置的新值是barbecue 设置前的值是beef

# r1.hset("hash1", "k1", "v1")
# r1.hset("hash1", "k2", "v2")
# print(r1.hkeys("hash1"))                   # 取hash中所有的key
# print(r1.hget("hash1", "k1"))              # 单个取hash的key对应的值
# print(r1.hmget("hash1", "k1", "k2"))       # 多个取hash的key对应的值
# r1.hsetnx("hash1", "k2", "v3")             # 只能新建
# print(r1.hget("hash1", "k2"))

# r1.hmset("hash2", {"k2": "v2", "k3": "v3"})
# print(r1.hget("hash2", "k2"))  # 单个取出"hash2"的key-k2对应的value
# print(r1.hmget("hash2", "k2", "k3"))  # 批量取出"hash2"的key-k2 k3对应的value --方式1
# print(r1.hmget("hash2", ["k2", "k3"]))  # 批量取出"hash2"的key-k2 k3对应的value --方式2

# print(r1.hgetall("hash1"))

print(r1.hgetall("hash1"))
r1.hset("hash1", "k2", "v222")   # 修改已有的key k2
r1.hset("hash1", "k11", "v1")   # 新增键值对 k11
r1.hdel("hash1", "k1")    # 删除一个键值对
print(r1.hgetall("hash1"))



