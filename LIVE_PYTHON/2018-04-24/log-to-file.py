#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/5/29 10:34
# @Author  : zhouyuyao
# @File    : log-to-file.py
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
import logging.handlers

# 定义日志级别，默认warning以上才会输出告警日志信息
# logging.basicConfig(level=logging.DEBUG)

# 日志输出格式，在当前目录下生成 myapp.log 存放日志输出信息
LOG_FILE = 'myapp.log'
handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes=1024 * 1024, backupCount=5, encoding='utf-8')  # 实例化handler
fmt = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s'

formatter = logging.Formatter(fmt)  # 实例化formatter
handler.setFormatter(formatter)  # 为handler添加formatter

logger = logging.getLogger('tst')  # 获取名为tst的logger
logger.addHandler(handler)  # 为logger添加handler
logger.setLevel(logging.DEBUG)


def hello():
    print("hello world")

def main():
    logger.info(u"开始运行 main() 函数")
    print("##"*10)
    hello()
    logger.info(u"执行 hello() 函数")
    try:
        a = 2/0
        f = open("demon1.py", "r")
    except Exception as e:
        logger.error("除数不能为 0")
    finally:
        logger.warning(u"该文件没有正常关闭")

if __name__ == '__main__':
    main()
