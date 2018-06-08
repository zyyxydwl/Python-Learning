#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/5/29 10:30
# @Author  : zhouyuyao
# @File    : demon2.py
'''
日志记录模块
日志的几个级别
debug
info
warning
error
critical
'''
import logging
# 定义日志级别，默认warning以上才会输出告警日志信息
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)    #本身

def hello():
    print("hello world")

def main():
    logger.info("开始执行main函数")
    print("##"*10)
    hello()
    logger.info("调用hello() 函数")
    try:
        a = 2/0
        f = open("demon1.py", "r")
    except Exception as e:
        logger.error("除数不能为0")
    finally:
        logger.warning("文件没有正常关闭")

if __name__ == '__main__':
    main()