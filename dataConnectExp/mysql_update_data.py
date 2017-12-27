#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time      :2017/11/26 22:12
#@Author    :zhouyuyao
#@File      :mysql_update_data.py

import codecs

import pymysql
def connect_mysql():
    db_config = {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'test',
        'passwd': 'test',
        'db': 'test',
        'charset': 'utf8'
    }
    cnx = pymysql.connect(**db_config)
    return cnx


if __name__ == '__main__':
    cnx = connect_mysql()

    sql = '''select *, (grade+60) as newGrade from Score where Grade <5;'''
    update = '''update Score set grade = grade + 60 where grade < 5;  '''
    try:
        cus_start = cnx.cursor()
        cus_start.execute(sql)
        result1 = cus_start.fetchall()
        print(len(result1))
        cus_start.close()

        cus_update = cnx.cursor()
        cus_update.execute(update)
        cus_update.close()

        cus_end = cnx.cursor()
        cus_end.execute(sql)
        result2 = cus_end.fetchall()
        print(len(result2))
        cus_end.close()

        cnx.commit()
    except Exception as e:
        cnx.rollback()
        print('error')
        raise e
    finally:
        cnx.close()
