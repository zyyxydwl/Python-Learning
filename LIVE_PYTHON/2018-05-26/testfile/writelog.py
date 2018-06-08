#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/5/28 22:44
# @Author  : zhouyuyao
# @File    : writelog.py
'''不断记录服务端输入的日志
实现>> 和>
'''
import time
import sys
from tracelogisfile import TraceLog

class Server(object):
    def printLog(self):
        print("start server\n")
        for i in range(100):
            print(i)
            time.sleep(0.1)
        print("end server\n")

if __name__ == '__main__':
    traceLog = TraceLog("main.log")
    traceLog.start()
    sys.stdout = traceLog
    sys.stderr = traceLog
    server = Server()
    server.printLog()

# 每当调用print的时候，底层就是在代用sys.stdout.write(str)
# sys.stdout.write() = traceLog.write()