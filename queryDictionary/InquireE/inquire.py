#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      : 2018/1/17 11:48
# @Author    : zhouyuyao
# @File      : inquire.py
import codecs

class InquireWord(object):
    def __init__(self):
        self.inquireFileName = "./dictionary.txt"

    def getWordExp(self,word):
        with codecs.open(self.inquireFileName,'r',encoding="utf8") as f:
            tmp = f.readlines()
            for i in tmp:
                tmp_list = i.split()
                if tmp_list[0].lower() == word.lower():
                    return tmp_list[1]
            else:
                return False
        pass


if __name__=="__main__":
    tmp = InquireWord()
    print(tmp.getWordExp("abandon"))


