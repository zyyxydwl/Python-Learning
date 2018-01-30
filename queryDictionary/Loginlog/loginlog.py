#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      : 2018/1/18 20:25
# @Author    : zhouyuyao
# @File      : loginlog.py
import codecs
import time

class LoginLog(object):
    def __init__(self):
        self.filename = "loginlog.txt"

    def writeOneLine(self,username):
        with codecs.open(self.filename,'a',encoding='utf8') as f:
            now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            f.write("{0} {1}".format(username,now_time))

