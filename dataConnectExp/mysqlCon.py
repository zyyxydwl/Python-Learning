#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time      :2017/11/20 21:15
#@Author    :zhouyuyao
#@File      :mysqlCon.py

import pymysql

# 链接数据库
# host 数据库IP
# port 数据库监听端口
# user 链接数据库用户
# passwd 用户密码
# db 数据库名
# charset 字符集  utf-8

# 打开数据库连接
db=pymysql.connect("数据库IP","链接数据库用户","用户密码","数据库名")

# def connect_mysql():
#     db_config= {
#         "host":"数据库IP",
#         "port": "3306",
#         "user": "链接数据库用户",
#         "passwd": "用户密码",
#         "db": "数据库名",
#         "charset": "utf8mb4"  # 注意不是utf-8
#     }
#     try:
#         zyy=pymysql.connect(**db_config)
#     except Exception as e:
#         raise e
#     return zyy
#
# connect_mysql()

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()

print("Database version : %s " % data)

# 关闭数据库连接
db.close()