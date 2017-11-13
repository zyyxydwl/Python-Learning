#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time      :2017/11/8 22:22
#@Author    :zhouyuyao
#@File      :classThree.py

# 类的私有变量
class A(object):
    _name='zhou'
    _sex='F'
    def hello(self):
        print(self._name)
        print(self._sex)

    def get_sex(self):
        return self._sex
a=A()
print(a._name)
a.hello()
print(a.get_sex())

# 1、_xx 以单下划线开头的表示的是protected类型的变量。
# 即保护类型只能允许其本身与子类进行访问。若内部变量标示，
# 如： 当使用“from M import”时，不会将以一个下划线开头的对象引入 。
#
# 2、__xx 双下划线的表示的是私有类型的变量。
# 只能允许这个类本身进行访问了，连子类也不可以用于命名一个类属性（类变量），
# 调用时名字被改变（在类FooBar内部，__boo变成_FooBar__boo,如self._FooBar__boo）
#
# 3、__xx__定义的是特列方法。
# 用户控制的命名空间内的变量或是属性，如init , __import__或是file 。
# 只有当文档有说明时使用，不要自己定义这类变量。 （就是说这些是python内部定义的变量名）
