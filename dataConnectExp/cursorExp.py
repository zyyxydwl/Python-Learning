#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :2017/11/21 21:22
# @Author    :zhouyuyao
# @File      :cursorExp.py
import pymysql


# 游标实际上是一种能从包括多条数据记录的结果几种每次提取一条记录的机制
# 游标总是与一条 sql 选择语句相关联
# 因为游标由结果集（可以是零条，一条或由相关的选择语句检索出的多条记录）
# 和结果集中指向特定记录的游标位置组成。
# 当决定对结果集进行处理时，必须声明一个指向该结果集的游标。

# cursor():创建游标对象
# close():关闭此游标对象
# fetchone():得到结果集的下一行
# fetchmany([size = cursor.arraysize]):得到结果集的下几行
# fetchall():得到结果集中剩下的所有行
# excute(sql[, args]):执行一个数据库查询或命令
# executemany (sql, args):执行多个数据库查询或命令

def connect_mysql():  # 创建一个包含connect方法参数的函数
    global zyy, zyy
    db_config = {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'test',
        'password': 'test',
        'db': 'test',
        'charset': 'utf8mb4'  # charset 可以只写 utf8，注意不是 utf-8
    }
    try:
        zyy = pymysql.connect(**db_config)  # 创建一个 pymysql 链接对象，并赋值给 变量 cms
    except Exception as e:
        print(e)
    return zyy


if __name__ == '__main__':
    number = []
    for i in range(1, 100):
        number.append(i)  # 创建一个包含 1 到 99 的列表
    insert_sql = 'insert into test(id) value(%s);'  # 执行插入语句，将 number 插入列表
    select_sql = 'select * from test;'  # 选择所有的表内容
    db = connect_mysql()  # 创建一个 PyMySQL 数据库链接对象
    cus = db.cursor()  # 创建一个游标对象
    try:
        cus.execute('drop table if exists test; create table test(id int not null);')  # 执行语句，如果存在删除，并创建
        cus.executemany(insert_sql, number)  # executemany(arg, para) 必须两个参数，第一个是 sql 语句，第二个是参数
        cus.execute(select_sql)  # execute(arg) 方法，执行

        result1 = cus.fetchone()  # fetchone()，选取一行内容输出
        print('result1：', result1)

        result2 = cus.fetchmany(4)  # fetchmany(arg) 指定选取的行数
        print('result2：', result2)

        result3 = cus.fetchall()  # fetchall() 从当前游标开始，读取所有行
        print('result3：', result3)

        cus.close()  # 关闭游标
        db.commit()  # 提交数据库，如果没有这个操作，插入的数据就不会成功
    except Exception as e:
        db.rollback()
        raise e
    finally:
        cus.close()
