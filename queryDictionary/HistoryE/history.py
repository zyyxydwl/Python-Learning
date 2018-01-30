#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      : 2018/1/17 11:28
# @Author    : zhouyuyao
# @File      : history.py
import codecs
import time

class History(object):
    def __init__(self):
        self.filename = './history.txt'

    def writeOnelog(self,username,word,wordexp):
        with codecs.open(self.filename,'a',encoding="utf8") as f:
            now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            f.write("{0} {1} {2} {3}\n".format(now_time,username,word,wordexp))
            pass

    def getHistory(self,username):
        with codecs.open(self.filename,'r',encoding="utf-8") as f:
            tmp = f.readlines()
            for i in tmp:
                tmp_list = i.split()
                if tmp_list[2] == username:
                    print(tmp_list)
        pass

if __name__=="__main__":
    tmp = History()
    # tmp.writeOnelog('aaa1','apple','苹果')
    tmp.getHistory('aaa1')

