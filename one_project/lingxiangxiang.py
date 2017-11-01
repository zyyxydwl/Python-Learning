#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/10/28 21:53
# @Author  : lingxiangxiang
# @File    : jc.py
'''1！ +2！ +3！ +…… + n!'''



def danyuan(n):
    sum = 1
    '''求n！  1*2*3*4*5*6*n'''
    if n == 0:
        print("0!= 1")
        return 1
    else:
        for i in xrange(1, n+1):
            sum *= i
        print("{0}! = {1}".format(i, sum))
        return sum

if __name__ == "__main__":
    import sys
    reload(sys)
    sys.setdefaultencoding("utf-8")

    n = input("plase inpurt number n(n>=0):")
    sum = 0
    for i in xrange(0, n+1):
        sum += danyuan(i)
    print("end main sum = {0}".format(sum))




