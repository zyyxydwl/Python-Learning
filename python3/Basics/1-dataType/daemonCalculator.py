#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/1/22 22:29
# @Author  : zhouyuyao
# @File    : daemonCalculator.py
# PyCharm 2017.3.2 (Community Edition)
# Build #PC-173.4127.16, built on December 19, 2017
# JRE: 1.8.0_152-release-1024-b8 amd64
# JVM: OpenJDK 64-Bit Server VM by JetBrains s.r.o
# Windows 10 10.0
# Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) 
# [MSC v.1900 64 bit (AMD64)] on win32

def add(string):
    total = 0
    numbers = []
    numbers += string.split("+")
    for num in numbers:
        total += int(num)
    print("{0}={1}".format(string,total))

def reduce(string):
    result = 0
    numbers = []
    numbers += string.split("-")
    result = int(numbers[0])
    numbers.pop(0)
    for num in numbers:
        result -= int(num)
    print("{0}={1}".format(string,result))

def ride(string):   # 乘
    total = 1
    numbers = []
    numbers += string.split("*")
    for num in numbers:
        total *= int(num.strip())
    print("{0}={1}".format(string,total))

def division(string):
    result = 0
    numbers = []
    numbers += string.split("/")
    result = int(numbers[0])
    numbers.pop(0)
    for num in numbers:
        result /= int(num.strip())
    print("{0}={1}".format(string,result))



if __name__ =="__main__":
    print("###############################")
    print("#####欢迎来到计算器工作中心######")
    print("###############################")
    print("1：加法 (a+b+c+d···)")
    print("2：减法 (a-b-c-d···)")
    print("3：乘法 (a*b*c*d···)")
    print("4：除法 (a/b/c/d···)")
    method = input("Please input number(1/2/3/4): ")
    if method == "1":
        string = input("请输入您的表达式：")
        add(string)
    elif method == "2":
        string = input("请输入您的表达式：")
        reduce(string)
    elif method == "3":
        string = input("请输入您的表达式：")
        ride(string)
    elif method == "4":
        string = input("请输入您的表达式：")
        division(string)
    else:
        print("The string you input is error.")

