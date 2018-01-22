#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.header import Header
import sys,smtplib

# 第三方 SMTP 服务
mail_host="smtp.exmail.qq.com"  #设置服务器
mail_user="monitor@17caipiao.com"    #用户名
mail_pass="pOLTG-X3EXu="   #口令 

# 定义收发地址
sender = 'monitor@17caipiao.com'
receivers = ['1162572407@qq.com','jiangdf@17caipiao.com','mayp@17caipiao.com']


def send_mail(message):
    try:
        smtpObj = SMTP_SSL(mail_host,465)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print "邮件发送成功"
    except smtplib.SMTPException:
        print "无法发送邮件"

if __name__ == '__main__':
    
    mail_ip=sys.argv[1] # 邮件来源
    mail_subject=sys.argv[2] # 邮件主题
    mail_content=sys.argv[3] #邮件内容
    
    
    # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
    message = MIMEText(mail_content, 'plain', 'utf-8')
    message['Subject'] = Header(mail_subject, 'utf-8')
    message['From'] = Header(mail_ip, 'utf-8')
    message['To'] =  Header("服务启动状态", 'utf-8')
 
    send_mail(message)
