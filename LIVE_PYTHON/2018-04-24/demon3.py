#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/5/29 16:47
# @Author  : zhouyuyao
# @File    : demon3.py
import logging.handlers


LOG_FILE = r'tst.log'

handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes=1024 * 1024, backupCount=5, encoding='utf-8')  # 实例化handler
fmt = '%(asctime)s - %(levelname)s - %(message)s'

formatter = logging.Formatter(fmt)  # 实例化formatter
handler.setFormatter(formatter)  # 为handler添加formatter

logger = logging.getLogger('tst')  # 获取名为tst的logger
logger.addHandler(handler)  # 为logger添加handler
logger.setLevel(logging.DEBUG)

logger.info(u'输出中文试一试')
logger.debug('first debug message')