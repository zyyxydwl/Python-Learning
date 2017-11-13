#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time      :2017/11/6 21:10
#@Author    :zhouyuyao
#@File      :classOne.py

# 类的一般形式
class ren(object):
    '''this class is about ren class。类的说明，使用三个单引号'''
    name='菇凉'
    sex='Female'
    def hello(self):
        print('hello world')

a=ren()
print(type(a))
print(a.name)
print(a.sex)
a.hello()
a.name='未来啊'
print(a.name)
# 返回结果
# <class '__main__.ren'>
# 菇凉
# Female
# hello world
# 未来啊


# 类的构造器
class ren():
    '''this class is about ren class。类的说明，使用三个单引号'''
    def __init__(self,name,sex):        # 构造器
        # 注意到 __init__ 方法的第一个参数永远是 self ，表示创建的实例本身
        # 因此，在 __init__ 方法内部，就可以把各种属性绑定到 self
        # 因为self 就指向创建的实例本身
        # 有了 __init__ 方法，在创建实例的时候，就不能传入空的参数了
        # 必须传入与 __init__ 方法匹配的参数，
        # 但 self 不需要传，python解释器会把实例变量传进去
        self.name=name
        self.sex=sex
    def hello(self):
        print('hello {0}'.format(self.name))

test=ren('zhouyuyao','F')     # 需输入参数
test.hello()
# 返回结果
# hello zhouyuyao

# 类的继承
class A(object):
    pass
class B(object):
    pass

class C(A,B):       # C 继承了 A 和 B
    pass

class parent():
    name='parent'
    age='50'
    def __init__(self):
        print('my name is {0}'.format(self.name))
        print('my age is {0}'.format(self.age))
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age

class child(parent):
    name = 'child'
    age = 10
    def __init__(self):
        print('my name is {0}'.format(self.name))
    def hello(self):
        print('hello world')

a=child()
a.hello()
a.get_name()
print(a.get_age())


