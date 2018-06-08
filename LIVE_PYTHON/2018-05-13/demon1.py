#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/5/13 23:30
# @Author  : zhouyuyao
# @File    : demon1.py

from sqlalchemy import create_engine, Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()
# declarative_base() 创建了一个 BaseModel 类，这个类的子类可以自动与一个表关联。
class Student(Base): # 必须继承declaraive_base得到的那个基类
    __tablename__ = 'student'
    # 必须要有__tablename__来指出这个类对应什么表，这个表可以暂时在库中不存在，SQLAlchemy会帮我们创建这个表
    id = Column(Integer, primary_key=True)   # Column类创建一个字段
    name = Column(String(100))
    age = Column(Integer)
    address = Column(String(100))


def update(session):
    student1 = session.query(Student).filter(Student.id == 1001).one()
    # session.query(Student) 显示SQL 语句
    # filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。
    # 该接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判，
    # 然后返回 True 或 False，最后将返回 True 的元素放到新列表中。
    student1.name='test123'
    session.commit()
    # 在SQLAlchemy中一个Session（可以看作）是一个transaction，每个操作（基本上）对应一条或多条SQL语句，
    # 这些SQL语句需要发送到数据库服务器才能被真正执行，而整个transaction需要commit才能真正生效，
    # 如果没提交，一旦程序挂了，所有未提交的事务都会被回滚到事务开始之前的状态。
    # flush就是把客户端尚未发送到数据库服务器的SQL语句发送过去，commit就是告诉数据库服务器提交事务。
    # 简单说，flush之后你才能在这个Session中看到效果，而commit之后你才能从其它Session中看到效果。
    student2 = session.query(Student).filter(Student.id == 1001).one()
    print(student2.name)

def delete(session):
    session.query(Student).filter(Student.id == 1001).delete()
    session.commit()

def insert(session):
    student1 = Student(id=1004, name='zyy', age=28, address='xiangtan')
    session.add(student1)
    session.commit()

def count(session):
    numnber = session.query(Student).filter().count()
    print("total student is {0}".format(numnber))

def groupBy(session):
    groupByAge = session.query(Student).group_by(Student.age).all()
    print(groupByAge)
    for i in groupByAge:
        print(i.id, i.name, i.age, i.address)

def orderBy(session):
    orderByAge = session.query(Student).order_by(Student.age.desc()).all()
    for x in orderByAge:
        print(x.id, x.name, x.age, x.address)

def main():
    # engine = create_engine('mysql+pymysql://username:passwd@xxx.xxx.xxx.xxx/databasename')
    engine = create_engine('mysql+pymysql://testdb:6ib9c9xyxk@120.78.233.114/TESTDB')
    DBsession = sessionmaker(bind=engine)
    session = DBsession()
    # insert(session)
    # update(session)
    # delete(session)
    # count(session)
    # groupBy(session)
    orderBy(session)

if __name__ == '__main__':
    # 一个python的文件有两种使用的方法，
    # 第一是直接作为脚本执行，
    # 第二是import到其他的python脚本中被调用（模块重用）执行
    # 在if__name__ == 'main': 下的代码只有在第一种情况下（即文件作为脚本直接执行）才会被执行，
    # 而import到其他脚本中是不会被执行的。
    main()


