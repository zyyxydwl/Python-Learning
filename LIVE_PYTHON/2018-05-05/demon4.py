#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/5/6 22:31
# @Author  : zhouyuyao
# @File    : demon4.py
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/5/6 22:04
# @Author  : zhouyuyao
# @File    : demon2.py
import pymysql

# 打开数据库连接
# db = pymysql.connect("***.***.***.***", "database-user", "database-UserPasswd", "database-name")
db = pymysql.connect("120.78.233.114", "testdb", "6ib9c9xyxk", "TESTDB")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute() 方法执行 SQL，如果表存在则删除
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# 使用预处理语句创建表
sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""

cursor.execute(sql)

# 关闭数据库连接
db.close()
