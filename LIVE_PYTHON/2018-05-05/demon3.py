#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/5/6 22:17
# @Author  : zhouyuyao
# @File    : demon3.py
import pymysql

class TestMysql(object):
    def __init__(self):
        self.dbConfig = {
            "host": "120.78.233.114",
            "port": 3306,
            "user": "testdb",
            "passwd": "6ib9c9xyxk",
            "db": "TESTDB"
        }
        conn = pymysql.connect(**self.dbConfig)
        # 当函数的参数前面有一个星号*的时候表示这是一个可变的位置参数，两个星号**表示是可变的关键字参数。
        self.a = conn

    def select(self):
        # print("select")
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = self.a.cursor()
        # 使用 execute()  方法执行 SQL 查询
        cursor1 = cursor.execute("SELECT VERSION()")
        self.cursor2 = cursor1

    def update(self):
        print("update")

if __name__ == '__main__':
    conn = TestMysql()
    print(conn.select())
