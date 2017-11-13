#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time      :2017/11/11 8:22
#@Author    :zhouyuyao
#@File      :osExp.py

# os 模块，可通过 os 调用系统命令

# 1、查看不同的操作系统
import os
print(os.name)
# 这个可以查看我们的系统类型
# win 系统则会输出 "nt"
# Linux 系统则会输出 "posix"

# 2、执行系统命令
# print(os.system("ipconfig"))
# win 的格式是 gkm
# 常用的是 utf-8
context=os.popen('ipconfig').read()       # popen 返回一个 file 对象，再使用read读出来
print(context.find('192.168.16.1'))       # 返回找到匹配项的字节处
# print(dir(os))          # 查看方法
# 3、文件和目录的操作

print(os.listdir('.'))
print(os.getcwd())           # 获得路径
print(os.listdir(os.getcwd()))
os.chdir('E:/GitHub/Python-Learning/modules')
print(os.getcwd())           # 当前目录切换到 D: 目录下

os.mkdir('test')             # 在 E:/GitHub/Python-Learning/modules 目录下创建一个 test 目录

if not os.path.exists('test'):
    os.makedirs('test')
else:
    print('test is exist')



