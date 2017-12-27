#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :2017/11/26 18:41
# @Author    :zhouyuyao
# @File      :cursorExp2.py


config1 = {
    'pool_name': 'test',
    'host': 'localhost',
    'port': 3306,
    'user': 'test',
    'password': 'test',
    'database': 'test'
}


def connection_pool():
    # Return a connection pool instance
    pool = connection_pool(**config)
    pool.connect()
    return pool


# 直接访问并获取一个 cursor 对象，自动 commit 模式会在这种方式下启用
with connection_pool().cursor() as cursor:
    print('Truncate table user')
    cursor.execute('TRUNCATE user')
    print('Insert one record')
    result = cursor.execute('INSERT INTO user (name, age) VALUES (%s, %s)', ('Jerry', 20))
    print(result, cursor.lastrowid)
    print('Insert multiple records')
    users = [(name, age) for name in ['Jacky', 'Mary', 'Micheal'] for age in range(10, 15)]
    result = cursor.executemany('INSERT INTO user (name, age) VALUES (%s, %s)', users)
    print(result)
    print('View items in table user')
    cursor.execute('SELECT * FROM user')
    for user in cursor:
        print(user)
    print('Update the name of one user in the table')
    cursor.execute('UPDATE user SET name="Chris", age=29 WHERE id = 16')
    cursor.execute('SELECT * FROM user ORDER BY id DESC LIMIT 1')
    print(cursor.fetchone())
    print('Delete the last record')
    cursor.execute('DELETE FROM user WHERE id = 16')
