from email.mime.text import MIMEText
msg=MIMEText('hello,world','plain','utf-8')

from_addr=input('邮箱地址：')
password=input('密码：')
to_addr=input('目标邮箱：')
smtp_server=input('SMTP server:')

import smtplib
server=smtplib.SMTP(smtp_server,25)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()

#邮箱地址：1204628226@qq.com
#密码：jhwieyruqdjajidh
#目标邮箱：ruan1204628226@sina.com
#SMTP server:smtp.qq.com