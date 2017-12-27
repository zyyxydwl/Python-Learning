#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :2017/11/26 18:39
# @Author    :zhouyuyao
# @File      :connectionExp.py



import pandas as pd
from PyMysqlPool import ConnectionPool

config = {
    'pool_name': 'test',
    'host': 'localhost',
    'port': 3306,
    'user': 'test',
    'password': 'test',
    'database': 'test'
}


def connection_pool():
    # Return a connection pool instance
    pool = ConnectionPool(**config)
    pool.connect()
    return pool


with connection_pool().connection() as conn:
    pd.read_sql('SELECT * FROM user', conn)
# 或者
connection = connection_pool().borrow_connection()
pd.read_sql('SELECT * FROM user', conn)
connection_pool().return_connection(connection)
