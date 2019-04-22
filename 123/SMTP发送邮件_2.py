from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr,formataddr
import smtplib
def _format_addr(s):
	name,addr=parseaddr(s)
	return formataddr((Header(name,'utf-8').encode(),addr))

from_addr=input('邮箱地址：')
password=input('密码:')
to_addr=input('目标邮箱：')
smtp_server=input('SMTP server:')

msg=MIMEText('hello world','plain','utf-8')
msg['From']=_format_addr('Python<%s>'%from_addr)
msg['To']=_format_addr('guanliyuan<%s>'%to_addr)
msg['Subject']=Header('来自SMTP的问候','utf-8').encode()

server=smtplib.SMTP(smtp_server,25)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()

#html邮件
#msg = MIMEText('<html><body><h1>Hello</h1>' +
#    '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
#   '</body></html>', 'html', 'utf-8'）
#将plain改为html
#带有标题的邮件