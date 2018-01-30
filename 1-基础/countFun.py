#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      : 2018/1/4 15:15
# @Author    : zhouyuyao
# @File      : countFun.py

# 1. 设计一个函数，统计任意一串字符串中数字字符的个数
# 例如：
# "adfdfjv1jl;2jlk1j2" 数字个数为3个

def countNum():
    co = 0
    s = input("Please input a string : ")
    for c in s:
        if c.isdigit():
            co+=1
    print("The string have {} number.".format(co))
countNum()


# 2. 设计函数，统计任意一串字符串中每个字母的个数，不区分大小写
# 例如：
# "aaabbbcccaae111"
# a 5个
# b 3个
# c 3个
# e 1个

# def countNum():******************test*****************/
#     co = 0
#     s = input("Please input a string : ")
#     s=s.lower()
#     for a in s:
#         if a.isalpha() and a in (chr(a) for a in range(97,122)):
#             co+=1
#     print("The string have {} character.".format(co))
# countNum()******************test*****************/

import re
def countNum():
    a={}
    # s1=''
    s = input("Please input a string : ")
    s1=re.sub('[^a-zA-Z]','',s)
    a = {i: s.count(i) for i in s1}
    print(a)
countNum()


# 去掉字符串中字母以外的字符，在Python编程语言中有多种实现方式。
#
# Python中的str类型，有一个isalpha()方法，判断字符是否是英文字符。可以使用循环逐个字符判断是否是英文字符，如果是英文字符则加入新的字符串。
# 1
# 2
# 3
# 4
# 5
# 6
# oldS = 'as30wejl2@2]sjls'
# newS = ''
# for s in oldS:
#     if s.isalpha():
#         newS += s
# print newS
# 以上代码可以使用表理解浓缩成一行，表理解返回的结果是一个list，因此需要用空字符串''连接。
#
# 1
# print ''.join([x for x in oldS if x.isalpha()])
# 上面的实现方式可以完成任务，但仍然不够凝练。最佳的实现方式是使用正则表达式匹配非英文字母，将其替换成空字符，这可以使用re包的sub()函数实现。
#
# 1
# 2
# import re
# print re.sub('[^a-zA-Z]','',oldS)
# 上述正则表达式[^a-zA-Z]，就是用于匹配非英文字符。






