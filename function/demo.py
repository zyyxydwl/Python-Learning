#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time      :2017/11/1 22:26
#@Author    :zhouyuyao
#@File      :demo.py

# 函数的定义

def sum(x,y):
    print('x={0}'.format(x))
    print('y={0}'.format(y))
    return x+y
m = sum(10,3)              # 调用定义的 sum 函数，x=10 y=3
print('x+y=%s' % m)        # 返回值 x+y=13

# 函数的参数
# 1、给 b 变量设定一个默认的值
# 如果实参传入的时候，指定了 b 的值，那 b 优先选择传入的实参，当 b 没有值时，才会用默认值
def funcA(a,b=0):
    print(a)
    print(b)
funcA(1)        # b 变量选择默认实参
funcA(10,20)    # b 变量选择传入实参

# 2、参数为 tuple
def funT(a,b,*c):
    print(a)
    print(b)
    print("length of c is : %d" % len(c))
    print(c)

funT(1,2,3,4,5,6)

# 3、参数为 dictionary
def funD(a,**b):
    print(a)
    for x in b:
        print(x + ":" + str(b[x]))
funD(100,x="hello",y="你好")
args={"1":"a","2":"b"}           # 定义一个字典
funD(100,**args)


