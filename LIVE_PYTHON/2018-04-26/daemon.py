#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/4/26 22:06
# @Author  : zhouyuyao
# @File    : daemon.py
# PyCharm 2017.3.2 (Community Edition)
# Build #PC-173.4127.16, built on December 19, 2017
# JRE: 1.8.0_152-release-1024-b8 amd64
# JVM: OpenJDK 64-Bit Server VM by JetBrains s.r.o
# Windows 10 10.0
# Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) 
# [MSC v.1900 64 bit (AMD64)] on win32
import codecs

# import requests
#
# url = 'http://item.jd.com/17812015666.html?sku=17812015666&shopid=0&enc=dTFbliUKvSmdZmujuZQ8bzjOdBDr_gUlMmJahJ5z5ru3nqlDnlgI65uBDwj-uWH6WOa2g1K9EdhuKyT9u5oExqNzEW9Qgtm81cMRJoLqFls%3D&tk=e89355666f27cc84d24bcd404c603a0c&share=1&fs=1&gt=1524751659&spu=17812015666&v=1&couponValue=10&couponId=113337465'
# session = requests.session()
# r = session.get(url)
# print(r.text)

import json

test = {"a":1,"b":2}

with codecs.open("1.txt","r") as f:
    json.dump(test,f)




