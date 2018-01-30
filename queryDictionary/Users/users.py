#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/1/22 10:13
# @Author  : zhouyuyao
# @File    : users.py
# PyCharm 2017.3.2 (Community Edition)
# Build #PC-173.4127.16, built on December 19, 2017
# JRE: 1.8.0_152-release-1024-b8 amd64
# JVM: OpenJDK 64-Bit Server VM by JetBrains s.r.o
# Windows 10 10.0
# Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) 
# [MSC v.1900 64 bit (AMD64)] on win32
import codecs

import time


class Users(object):
    def __init__(self):
        self.userFileName = "./user.txt"

    def login(self, userName, userPasswd):
        with codecs.open(self.userFileName,"r",encoding="utf-8") as f:
            tmp = f.readlines()
            for i in tmp:
                list_tmp = i.split()
                if list_tmp[0] == userName and list_tmp[1] == userPasswd:  # 登录成功
                    return "Success."
                elif list_tmp[0] == userName and list_tmp[1] != userPasswd:
                    return "Wrong."
            return "NotFound."

    def register(self,userName,userPasswd):
        with codecs.open(self.userFileName, "r", encoding="utf-8") as f:
            tmp = f.readlines()
            for i in tmp:
                list_tmp = i.split()
                if list_tmp[0]==userName:
                    return "The username was exist."

        with codecs.open(self.userFileName,"a",encoding="utf-8") as f:
            now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            f.writelines("{0} {1} {2}\n".format(userName,userPasswd,now_time))
        return "Register Success."

if __name__ =="__main__":
    user1 = Users()
    print("{0}".format(user1.register("test223","123241")))












