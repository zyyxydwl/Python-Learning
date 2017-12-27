#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      : 2017/12/26 20:51
# @Author    : zhouyuyao
# @File      : countNumber.py


# 3.ABCD*9=DCBA,求A=?,B=?,C=?,D=?
# 面向对象，一定要考虑到怎样封装
#
class CountNumber(object):
    '''ABCD * 9 = DCBA
    通过计算机的方法，计算出A=?,B=?,C=?,D=?
    A:1-9
    B:0-9
    C:0-9
    D:1-9
    A != B != C != D
    '''
    def __init__(self):
        print("ABCD* 9 = DCBA;A!=B!=C!=D")
    def numAbcd(self):
        for A in range(1,10):
            for B in range(0,10):
                for C in range(1,10):
                    for D in range(0,10):
                        if (A*1000 + B*100 + C*10 + D*1)*9==(D*1000 + C*100 + B*10 + A*1):
                            print("{0}{1}{2}{3} * 9 = {4}{5}{6}{7}".format(A,B,C,D,D,C,B,A))
                            print("A={},B={},C={},D={}".format(A,B,C,D))


def main():
    countNumber = CountNumber()         #如等号前为灰色字体说明还未被调用
    countNumber.numAbcd()

if __name__==("__main__"):
    main()

