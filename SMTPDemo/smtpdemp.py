'''SMTP 发送邮件'''
from email.mime.text import MIMEText
import smtplib

message = MIMEText('hello, send by python...', 'plain', 'utf-8')

from_addr = input('From:')
password = input('password:')
to_addr = input('To:')
smtp_server = input('SMTP Server:')

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], message.as_string())
server.quit()
