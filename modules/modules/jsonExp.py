#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :2017/11/13 21:17
# @Author    :zhouyuyao
# @File      :jsonExp.py

# Javascript Object Notation，对象符号，是一种轻量级的数据交换格式
# 广泛应用于 AJAX 中 web 服务器和客户端的通讯的数据格式
# 也常用于 http 请求中
#
# json 四种方法
# 用来处理字符串
#     json.loads()     # 加载，把 json 转换成其他格式
#     json.dumps()     # 颠倒，把其他格式转换成 json
# 用来处理文件的
#     json.load()      # 加载，把 json 转换成文件或其他格式
#     json.dump()      # 颠倒，把文件等其他格式转换成 json
#
# EXp: 把 python 的 dict 格式转换成 json 字符串格式
import json

a = dict(name='zhouyuyao', age='21', message='you are so beautiful')
print(a)
print(type(a))     # <class 'dict'>
b = json.dumps(a)  # 字典转换成字符串
print(b)
print(type(b))     # <class 'str'>

c=json.loads(b)    # 字符串转换成字典
print(c)
print(type(c))     # <class 'dict'>
print(c['name'])

# 文件相关
# load 是从文件中中拿 json 数据，把文件转换成 json 数据
# dump 就是把 json 数据写入到文件中
import json

jsondata='{"a":1,"b":2,"c":3}'
with open('a.txt','w') as f:
    json.dump(jsondata,f)

with open('a.txt','r') as fr:
    m=json.load(fr)
    print(m)

