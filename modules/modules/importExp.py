#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time      :2017/11/9 21:02
#@Author    :zhouyuyao
#@File      :import.py

import codecs       # import 就是引入别人写的模块

with codecs.open('1.txt','w') as f:
    pass

import zhouyuyao.test
zhouyuyao.test.hello()

from zhouyuyao import test
test.hello()

# import 一般我们用作导入模块使用，常用的快捷键是 Alt+enter 可以直接导入模块

from zhouyuyao.test import  hello
hello()

# from ······ import ······ 这个是从什么模块中导入什么
# 最终你可以导入的是函数，也可以是一个类，也可以是一个模块
# 就最终结果应该是一一对应一层层调用

