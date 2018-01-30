#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      : 2018/1/17 11:57
# @Author    : zhouyuyao
# @File      : interface.py

class Interface(object):
    def main(self):
        print('''
*************************
*   English Dictionary  *
*************************
*        1. Login       *
*        2. Regist      *
*        3. Quit        *
*************************
        ''')

    def login(self):
        print('''
*************************
*          Login        *
*************************
        ''')

    def register(self):
        print('''
*************************
*        Register       *
*************************
        ''')

    def inquire(self):
        print('''
*************************
*         Inquire       *
*************************
*        1. History     *
*        2. Back        *
*        3. Quit        *
*************************
        ''')

    def historyInterface(self):
        print('''
*************************
*     History Record    *
*************************
        ''')

if __name__ == "__main__":
    tmp = Interface()
    tmp.main()
    tmp.historyInterface()

