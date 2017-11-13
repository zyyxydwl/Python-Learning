#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time      :2017/11/13 20:37
#@Author    :zhouyuyao
#@File      :sysExp.py

# ansible -i 1.txt all -m shell -a 'w'
# sys.argv[n] 可以获取到 python 脚本后面传进去的参数
import sys

if __name__ == '__main__':
    print('sys.argv[0]={0}'.format(sys.argv[1]))
    print('sys.argv[1]={0}'.format(sys.argv[2]))
    print('sys.argv[2]={0}'.format(sys.argv[3]))
# 此处需先设置参数或后添加参数
    sys.stdout.write('hello zhouyuyao\n')
    print('hello world')
    name=input("Please input your name: ")
    print("hello " + name)
    age=sys.stdin.readline()
    print(age)

f=open('w.log','w')
sys.stdout=f
print('qwerty')
print('hello zhouyuyao')

# sys.exit(n)
def hello():
    print('helo hello')
    sys.exit()

