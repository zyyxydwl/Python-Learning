#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time      :2017/11/7 22:04
#@Author    :zhouyuyao
#@File      :classTwo.py

# 类的重写
# 子类除了继承父类的所有属性和方法，还可以自定义自己的属性和方法，大大增加了代码的复用性
class parent(object):
    name='parent'
    sex='F'
    def __init__(self):
        print('my name is {0}'.format(self.name))
        print('my name is parent')
    def get_name(self):
        return self.name
    def get_sex(self):
        return self.sex

class child(parent):
    age = '21'
    # age = 10
    def __init__(self):
        super(child,self).__init__()
        print('my age is {0}'.format(self.age))
    def hello(self):
        print('hello world')
    def get_name(self):
        print('today is a nice day')

a=child()      # 初始化语句
a.hello()
a.get_name()
a.get_sex()
# 返回结果：
# my name is parent
# my name is parent
# my age is 21
# hello world
# today is a nice day


# Python类的继承注意事项：
# 1、在继承中类的构造(__init__()方法)不会自动调用，它需要在子类的构造中亲自调用。
# 2、Python总是首先子类中的方法，如果子类没有找到，才回去父类中查找。







