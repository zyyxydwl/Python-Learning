#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/6/4 14:04
# @Author  : zhouyuyao
# @File    : client2.py
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 9999
address = (host, port)
s.connect(address)
flage = 1
print("start client!")
while flage:
    word = input("word: ")
    if word == "exit":
        flage = 0
    s.sendall(word.encode('utf-8'))
    data = s.recv(2048)
    print("RECV: {0}".format(data.decode('utf-8')))

s.close()

'''
start client!
word: hello
RECV: HELLO
word: 你好吗
RECV: 你好吗
'''
