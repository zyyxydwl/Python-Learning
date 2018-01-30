#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      : 2018/1/17 11:19
# @Author    : zhouyuyao
# @File      : login.py

from HistoryE.history import History
from InquireE.inquire import InquireWord
from Interface.interface import Interface
from Loginlog.loginlog import LoginLog
from Userinput.userinput import UserInput
from Users.users import Users


class EnglishDictionary(object):
    def __init__(self):
        self.state = "Main"  # 当前状态
        self.UserName = None  # 用户名
        self.passwd = None  # 密码
        self.history = History()  # 实例化
        self.inquire = InquireWord()
        self.interface = Interface()
        self.loginlog = LoginLog()
        self.userinput = UserInput()
        self.users = Users()

    def running(self):
        while True:
            if self.state == "Main":  # 主界面
                self.interface.main()  # 显示主界面
                while True:
                    self.userinput.Main()  # 获取主界面输入
                    if self.userinput.main == "1":
                        self.state = "LogoIn"  # 切换到登录界面
                        break
                    elif self.userinput.main == "2":
                        self.state = "Regist"  # 切换到注册界面
                        break
                    elif self.userinput.main == "3":
                        exit(0)  # 退出程序

            elif self.state == "LoginIn":
                self.interface.login()  # 显示登录界面
                while True:
                    self.UserName = self.userinput.UserName()  # 获取用户名
                    self.passwd = self.userinput.passwd()  # 获取密码
                    result = self.users.login(self.UserName, self.passwd)
                    if result == "Success":
                        self.loginlog.writeOneLine(self.UserName)  # 写入日志
                        print("Login Success!")
                        self.state = "Inquire"
                        break
                    elif result == "Wrong":
                        print("wrong password!")
                    else:
                        print("user was not found.")

            elif self.state == "Regist":  # 注册界面
                self.interface.register()
                while True:
                    self.UserName = self.userinput.UserName()  # 获取用户名
                    self.passwd = self.userinput.passwd()  # 获取密码
                    result = self.users.register(self.UserName, self.passwd)  # 获取注册结果
                    if result == "Success":
                        print("Register Success!")
                        self.state = "Main"  # 注册成功，回到主界面
                        break
                    else:
                        print("User already exists.")
            elif self.state == "Inquire":  # 查询界面
                self.interface.inquire()  # 显示查询界面
                while True:
                    tmp = input("Please choose operater: ")  # 接收输入
                    if tmp == "1":  # 查询历史记录
                        self.history.getHistory(self.UserName)
                        continue
                    elif tmp == "2":  # 回到主菜单
                        self.state = "Main"
                        break
                    elif tmp == "3":  # 退出
                        exit(0)
                    else:
                        result = self.inquire.getWordExp(tmp)
                        if result != False:
                            print(result)
                            print(type(result), type(tmp))
                            self.history.writeOnelog(self.UserName, tmp, result)
                        else:
                            print("Sorry,word not found.")


if __name__ == "__main":
    client = EnglishDictionary()
    client.running()

#
#     def getWordExplanation(self):
#         with codecs.open("./user.txt", "r", encoding="utf-8") as f:
#             while True:
#                 tmp = f.readline()
#                 self.running()
#                 if tmp:
#                     list_tmp = tmp.split()
#                     if list_tmp[0].upper() < self.username.upper():
#                         continue
#                     elif list_tmp[0].upper() == self.username.upper():
#                         return list_tmp[1]
#                     else:
#                         return False
#                 else:
#                     return False
#
#     def running(self):
#         while True:
#             self.username = input("Please input your user name : ")
#             self.passwd = input("Please input your password : ")
#             if 4<=len(self.username) <=10 and self.username.isalnum():
#                 self.username = str(self.username)
#                 if 4<=len(self.passwd) <=10 and self.passwd.isalnum():
#                     self.passwd = str(self.passwd)
#                     self.register()
#                 else:
#                     print("Your passwd must have capitals、numbers only,and between 4-10 charac.")
#                     continue
#             else:
#                 print("Your username or passwd must have capitals、numbers only, and between 4-10 charac.")
#                 continue
#
#             self.username = str(self.username)
#             self.passwd = str(self.passwd)
#
#     def register(self):
#             result = self.getWordExplanation()
#             if result != False:
#                 print("该用户已注册，请直接登录")
#                 # self.logIn()
#             else:
#                 with codecs.open("user.txt", "a+") as f:  # 写入的方式打开文件
#                     f.writelines(self.username + ' ' + self.passwd  + ' ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "\n")  # 写入第一行
#                     print("Your username is {}".format(self.username))
#                     print("Your password is {}".format(self.passwd))
#                     print("注册成功")
#
#     def logIn(self):
#         pass
#
#
# w=EnglishDictionary()
# w.running()
# # w.register()
