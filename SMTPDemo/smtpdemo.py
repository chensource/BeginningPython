'''SMTP 发送邮件'''
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr = input('From:')
#密码必须使用授权码
password = input('password:')
to_addr = input('To:')
smtp_server = input('SMTP Server:')
message = MIMEText('hello, send by python...', 'plain', 'utf-8')
message['From'] = _format_addr('Python 爱好者 <%s>' % from_addr)
message['To'] = _format_addr('管理员 <%s>' % to_addr)
message['Subject'] = Header('陈同学的Python邮件测试..','utf-8').encode()
try:
    server = smtplib.SMTP(smtp_server, 587)
    server.starttls()
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], message.as_string())
    server.quit()
except Exception as e:
    print(str(e))
