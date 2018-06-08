#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/6/5 22:10
# @Author  : zhouyuyao
# @File    : demon2.py
import email.mime.multipart
import email.mime.text
import smtplib

msg = email.mime.multipart.MIMEMultipart()
msg['from'] = 'xxxxxxxx@163.com'
msg['to'] =  'xxxxxxxx@qq.com'
msg['subject'] = 'Have a good day.'    # 主题

context = '''
    <h1>晚上好</h1>
    你好，
     这是一封自动发送的邮件，请勿直接回复。
      www.ustchacker.com hello
    '''
text = email.mime.text.MIMEText(_text=context, _subtype="html")
msg.attach(text)

em = smtplib.SMTP_SSL()
em.connect("smtp.163.com", 465)
em.login("xxxxxxxx@163.com", 'xxxxxxxx')
em.sendmail(from_addr='xxxxxxxx@163.com', to_addrs='xxxxxxxx@qq.com', msg=msg.as_string())
em.quit()
