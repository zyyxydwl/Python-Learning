#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time      :2017/10/27 22:15
#@Author    :zhouyuyao
#@File      :file_write.py
import codecs
# mode 有几个参数需要注意：
# r 读
# w 写
# b 二进制
# a 追加

f=codecs.open('w2.txt','a')

f.write('Hello world\n')
f.write('Hello {0}\n'.format('zhouyuyao'))
f.write('Hello %s\n' %'future')
f.write('Never give up\n')
f.write('Never forget why you started \n')
f.close()


