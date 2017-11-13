#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :2017/11/3 19:02
# @Author    :zhouyuyao
# @File      :createList.py

# 列表生成式是 python 受欢迎的语法之一
# 通过一句简洁的语法就可以对一组元素进行过滤
# 还可以对得到的元素进行转换处理。

li = [x + x for x in range(1, 101) if x % 2 == 0]
print(li)

def funa(x):
    a=[]
    for x in range(1, 101):
        if x % 2 == 0:
            a.append(x+x)
    return a
print(funa(1))

# 列表生成器
# 1、最简单的办法，把原来的生成式的 [] 换成 () 就 ok 了
lt=(x*x for x in range(1,11) if x%2==0)
print(list(lt))
print(type(lt))
for i in lt:
    print(i)

# 2、函数中定义列表生成器
def fib(n):
    sum=0
    i=0
    while(i<n):
        sum=sum+i
        i+=1
        yield (sum)
print(type(fib(10)))
for x in fib(10):
    print(x)
print(type(fib(10)))

# 生成器和生成式的区别：
# 列表生成式，一次性生成所有的数据，然后保存在内存中，适合小量的数据
# 生成器，返回一个可以迭代的对象，及 'generator' 对象，必须通过循环才可以一一取出所以的结果
# 可迭代对象，可以通过循环调用出来的，就是可迭代的对象 [] () {} 生成式 生成器
# 迭代器  生成器，必须通过 next() 调用的，被 next() 函数调用并不断返回下一个值得对象称为迭代器

