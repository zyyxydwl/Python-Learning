#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/5/6 22:04
# @Author  : zhouyuyao
# @File    : demon2.py
import pymysql

# 打开数据库连接
db = pymysql.connect("***.***.***.***", "database-user", "database-UserPasswd", "database-name")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()

print("Database version : {0} ".format(data),end='')   # 输出为元组
# print ("Database version : %s " % data)              # 输出为字符串

# 关闭数据库连接
db.close()
