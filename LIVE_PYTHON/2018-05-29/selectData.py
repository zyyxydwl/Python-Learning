#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/5/30 13:47
# @Author  : zhouyuyao
# @File    : selectData.py
from sqlalchemy import create_engine, Integer, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://testdb:6ib9c9xyxk@120.78.233.114/sqlalchemy?charset=utf8')

Base = declarative_base()
class Dictionary(Base):
    __tablename__ = 'dictionary'
    id = Column(Integer, primary_key=True)
    key = Column(String(50))
    value = Column(String(50))

# class Dictionary(Base):
#     __tablename__ = 'dictionary'
#     __table_args__ = {
#         'mysql_engine': 'InnoDB',
#         'mysql_charset': 'utf8mb4'
#     }
#     id = Column(Integer, primary_key=True)
#     key = Column(String(50))
#     value = Column(String(50))

DBSession = sessionmaker(bind=engine)
session = DBSession()

while 1:
    word = input("please input your a word(exit with 'q'):")
    result =session.query(Dictionary).filter(Dictionary.key.like("{0}".format(word))).all()
    for each in result:
        print(each.id, each.key, each.value)
    if word == "q":
        exit(0)
