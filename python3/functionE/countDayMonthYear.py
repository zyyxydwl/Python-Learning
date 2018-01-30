#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/1/28 22:30
# @Author  : zhouyuyao
# @File    : countDayMonthYear.py
# PyCharm 2017.3.2 (Community Edition)
# Build #PC-173.4127.16, built on December 19, 2017
# JRE: 1.8.0_152-release-1024-b8 amd64
# JVM: OpenJDK 64-Bit Server VM by JetBrains s.r.o
# Windows 10 10.0
# Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) 
# [MSC v.1900 64 bit (AMD64)] on win32
from calendar import month

leapYear = dict()         # 申明month为字典
# 闰年
a = {"1":31,"2":28,"3":31,"4":30,"5":31,"6":30,"7":31,"8":31,"9":30,"10":31,"11":30,"12":31}
# 平年
b = {"1":31,"2":29,"3":31,"4":30,"5":31,"6":30,"7":31,"8":31,"9":30,"10":31,"11":30,"12":31}

leapYear["yes"] = b
leapYear["no"] = a
print(leapYear)


def panduan(year):
    if (int(year) %4==0 and int(year)%100!=0) or int(year) % 400 ==0:
        return True
    else:
        return False

def isint(date):
    year,leapYear,day = date.split("-")
    if int(year) <0:
        return False
    if month not in range(1,13):
        return False
    if panduan(int(year)):
        for i in leapYear["yes"].keys():
            if month == i:
                if int(day) >0 and int(day) <leapYear["yes"][i]:
                    return True
                else:
                    return False
    else:
        for i in leapYear["no"].keys():
            if month == i :
                if int(day) >0 and int(day)<=leapYear["no"][month]:
                    return True
    # except Exception as e:
    #     return False


def countdays(date):
    days = 0
    year,leapYear,day = date.split("-")
    if panduan(int(year)):
        # if int(month) <3:
        #     days = 31 + day
        #     print("{0}是今年的第{1}天".format(date,days))
        # else:
        for i in range(1,int(month)):
            days += leapYear["yes"][str(i)]
        days += int(day)
        print("{0}是今年的第{1}天".format(date,days))
    else:
        for i in range(1, int(month)):
            days += leapYear["no"][str(i)]
        days += int(day)
        print("{0}是今年的第{1}天".format(date, days))



def main():
    date = input("date(like 1970-1-1):")
    ok = isint(date)
    if ok:
        countdays(date)
    else:
        print("您的输入有误")

if __name__ == '__main__':
    main()

