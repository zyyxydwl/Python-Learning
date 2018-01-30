#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      : 2018/1/18 20:30
# @Author    : zhouyuyao
# @File      : userinput.py

class UserInput(object):

    def username(self):
        self.username = input("Please input your user name : ")
        self.passwd = input("Please input your password : ")
        if 4 <= len(self.username) <= 10 and self.username.isalnum():
            self.username = str(self.username)
        else:
            print("Your username must have capitals、numbers only, and between 4-10 charac.")
        self.username = str(self.username)

    def passwd(self):
        self.username = input("Please input your user name : ")
        self.passwd = input("Please input your password : ")
        if 4 <= len(self.username) <= 10 and self.username.isalnum():
            self.username = str(self.username)
        else:
            print("Your username must have capitals、numbers only, and between 4-10 charac.")
        self.username = str(self.username)

    def Main(self):
        while True:
            self.main = input("Please choose operation: ")  #接收输入
            if self.main in ["1","2","3"]:
                break



