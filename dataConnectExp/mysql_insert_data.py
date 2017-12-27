#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :2017/11/26 20:34
# @Author    :zhouyuyao
# @File      :mysql_insert_data.py

import pymysql

conn = pymysql.connect("127.0.0.1", "test", "test", "test")

cur = conn.cursor()

sqli = "insert into student values (%s,%s,%s,%s,%s);"
cur.execute(sqli, ("__NEXTVALUE()", "test", "21", "1996-05-20", "2017-11-26 21:41:00"))

cur.close()
cur.commit()
conn.close()

# 一次插入多条记录
sqli = "insert into student values(%s,%s,%s,%s);"
cur.executemany(sqli, [
    ('__NEXTVALUE()', 'Tom', '15', '2017-11-26 21:41:00', '2017-11-26 21:41:00'),
    ('__NEXTVALUE()', 'Jack', '31', '2017-11-26 21:41:00', '2017-11-26 21:41:00'),
    ('__NEXTVALUE()', 'Yaheng', '45', '2017-11-26 21:41:00', '2017-11-26 21:41:00'),
])
