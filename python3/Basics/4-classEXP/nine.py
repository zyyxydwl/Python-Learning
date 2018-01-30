#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/1/28 17:25
# @Author  : zhouyuyao
# @File    : nine.py
# PyCharm 2017.3.2 (Community Edition)
# Build #PC-173.4127.16, built on December 19, 2017
# JRE: 1.8.0_152-release-1024-b8 amd64
# JVM: OpenJDK 64-Bit Server VM by JetBrains s.r.o
# Windows 10 10.0
# Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) 
# [MSC v.1900 64 bit (AMD64)] on win32

'''
九宫格
____________
|_A_|_B_|_C_|
|_D_|_E_|_F_|
|_G_|_H_|_I_|
如果A取1到9，B则只能在1到9中取出A的值，C的值则从1到9中取出A和B，
每个数的取值都从1到9中取值，然后加入条件，这九个数之间存在的联系，
其一：9个数都不能相等，
其二：行和列每三个的数相加等于15

该算法比较慢，大概需要计算10的10次幂
'''
number = list()
for i in range(1,10):
    number.append(i)

for A in number:
    for B in number:
        for C in number:
            for D in number:
                for E in number:
                    for F in number:
                        for G in number:
                            for H in number:
                                for I in number:
                                    s = set()
                                    s.add(A)
                                    s.add(B)
                                    s.add(C)
                                    s.add(D)
                                    s.add(E)
                                    s.add(F)
                                    s.add(G)
                                    s.add(H)
                                    s.add(I)
                                    if (A+B+C) == (D+E+F) == (G+H+I) == (A+D+G) == (B+E+H) == (C+F+I) == (A+E+I) == (C+E+G) ==15 and len(s)==9:
                                        print("""
__________________
|_{0}_|_{1}_|_{2}_|
|_{3}_|_{4}_|_{5}_|
|_{6}_|_{7}_|_{8}_|""".format(A,B,C,D,E,F,G,H,I))











