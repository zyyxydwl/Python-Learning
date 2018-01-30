#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      : 2017/12/28 11:38
# @Author    : zhouyuyao
# @File      : pingpong.py



# 3. 两个乒乓球队进行比赛,各出三人。甲队为a,b,c三人,乙队为x,y,z三人。
# 已抽签决定比赛名单。有人向队员打听比赛的名单。
# a说他不和x比,c说他不和x,z比,请编程序找出三队赛手的名单。

equ1=list()
team1=['a','b','c']
team2=['x','y','z']
for i in range(0,3):
    for v in range(0,3):
        equ1.append([team1[i]+team2[v]])
equ1.remove(['ax'])    #a不和x比
equ1.remove(['cx'])    #c不和x比
equ1.remove(['cz'])    #c不和z比，c和y比
equ1.remove(['ay'])    #a不和y比
equ1.remove(['by'])    #b不和y比，a和z比
equ1.remove(['bz'])    #b不和z比

print(equ1)

# 二种解法，来自网络
for a in ['x','y','z']:
    for b in ['x', 'y', 'z']:
        for c in ['x', 'y', 'z']:
            if(a!=b)and(b!=c)and(c!=a) and (a!='x') and (c!='x') and (c!='z'):
                print('a和%s比赛，b和%s比赛，c和%s比赛' %(a,b,c))
