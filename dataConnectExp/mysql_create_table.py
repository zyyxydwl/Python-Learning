#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :2017/11/25 20:08
# @Author    :zhouyuyao
# @File      :mysql_create_table.py

import pymysql


def createTable(config):
    conn = pymysql.connect(**config)
    # print(conn)
    cur = conn.cursor()

    tb1 = 'STUDENT'
    # drop the table first if exist
    stmt_drop = "DROP TABLE IF EXISTS {0}".format(tb1)
    print("Drop table SQL : ", stmt_drop)

    # create new table
    stmt_create = (
        "CREATE TABLE {0} ("
        "    ID TINYINT UNSIGNED NOT NULL AUTO_INCREMENT, "
        "    NAME VARCHAR(50) DEFAULT '' NOT NULL, "
        "    AGE TINYINT DEFAULT NULL, "
        "    BRD date DEFAULT NULL, "
        "    CREATEDT datetime DEFAULT NULL, "
        "    PRIMARY KEY (ID))"
    ).format(tb1)

    print("Create SQL : ", stmt_create)

    cur.execute(stmt_create)

    cur.close()
    conn.close()


if __name__ == '__main__':
    config = {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'test',
        'password': 'test',
        'db': 'test',
        'charset': 'utf8mb4'  # charset 可以只写 utf8，注意不是 utf-8
    }
    createTable(config)
