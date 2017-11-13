#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :2017/11/11 7:00
# @Author    :zhouyuyao
# @File      :logging.py

import logging

def main():
    # Configure the logging system
    logging.basicConfig(
        filename='app.log',
        level=logging.WARNING,
        format='%(asctime)s:%(levelname)s:%(message)s')

    # Variables (to make the calls that follow work)
    hostname = 'www.zhouyuyao.cn'
    item = 'zyy'
    filename = 'index.php1'
    mode = 'r'

    # Example logging calls (insert into your program)
    logging.critical('Host %s unknown', hostname)
    logging.error("Couldn't find %r", item)
    logging.warning('Feature is deprecated')
    logging.info('Opening file %r, mode=%r', filename, mode)
    logging.debug('Got here')


if __name__ == '__main__':
    main()

# 从上往下，日志级别逐渐升高，debug —> info —> warning —> error —> critical


# 日志级别
#
# 级别	何时使用
# DEBUG	详细信息，典型地调试问题时会感兴趣。
# INFO	证明事情按预期工作。
# WARNING	表明发生了一些意外，或者不久的将来会发生问题（如‘磁盘满了’）。软件还是在正常工作。
# ERROR	由于更严重的问题，软件已不能执行一些功能了。
# CRITICAL	严重错误，表明软件已不能继续运行了。
#
# 作者：好吃的野菜
# 链接：http://www.jianshu.com/p/feb86c06c4f4
# 來源：简书
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
