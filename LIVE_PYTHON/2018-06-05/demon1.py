#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/6/5 20:36
# @Author  : zhouyuyao
# @File    : demon1.py

'''
1、遗留题目
2、socket 简介 服务
3、nginx 的 use epoll 模型
4、epolIO多路复用
5、select
6、python发送邮件
7、email   smtplib

'''
import yagmail
args={
    "user":"xxxxxxx@163.com",
    "password":"xxxxxxxx",
    "host":"smtp.163.com",
    "port":"465"
}
yagmail.SMTP(**args)

emailList=["xxxxxxx@qq.com"]
emailCc=['xxx@xxxxxxx.cn']
contenntS=["Have a good day.","1.txt","./theWayToGo.png"]

email = yagmail.SMTP(**args)
email.send(to=emailList,subject="Check",contents=contenntS,attachments="1.txt",cc=emailCc)
