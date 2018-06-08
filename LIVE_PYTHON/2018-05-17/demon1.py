#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/5/17 20:41
# @Author  : zhouyuyao
# @File    : demon1.py

'''

字符串的操作

get
set
mget
mset

list 的操作
r.lpush(name,value)  左边添加
r.rpush  右边添加
r.linsert  插入
lpop(name) 左边删除
r.lrange(name,start,end)  通过分片取list中的值
lset(name,index,value)  修改list中的某个值
lrem(name,value,num) 删除指定的值，
num默认为0，删除所有，num=2 从左往右删除两个元素，num=-1，从右往左删除1个元素

set操作
sadd()  增加
scard() 获取
s.pop   s.srem 删除
sunion()  并集


hash  主要掌握string 和 hash操作
获取key 的详细内容 hgetall(name)
设置单个元素 hset
设置多个元素 hmset
获取单个元素 hget
获取多个元素 hmset

获取所有的key  hkeys
获取所有的value hvals
判断key是否存在 hexists
删除key   hdel



其他常用操作
r.keys()  查看所有的key
r.delete(names)  删除keys
e.exists(name)   判断是否存在key
r.rename(src,dst)  新替换旧名字
r.expire(name,time)  设置超时时间




'''

