#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time      :2017/11/26 22:07
#@Author    :zhouyuyao
#@File      :mysql_delete_data.py

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

    sql = '''delete from student where id in(5,7)
    '''
    try:
        cus = cnx.cursor()
        cus.execute(sql)
        result = cus.fetchall()
        cus.close()
        cnx.commit()
    except Exception as e:
        cnx.rollback()
        print('error')
        raise e
    finally:
        cnx.close()





