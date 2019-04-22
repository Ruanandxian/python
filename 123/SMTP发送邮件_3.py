from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr,formataddr
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
import smtplib

def _format_addr(s):
	name,addr=parseaddr(s)
	return formataddr((Header(name,'utf-8').encode(),addr))

from_addr=input('邮箱地址：')
password=input('密码:')
to_addr=input('目标邮箱：')
smtp_server=input('SMTP server:')

#邮件对象
msg=MIMEMultipart()
msg['From']=_format_addr('Python   123<%s>'%from_addr)
msg['To']=_format_addr('ninini<%s>'%to_addr)
msg['Subject']=Header('laizi ni ma de wen hou ','utf-8').encode()

#邮件正文是MIMEText
msg.attach(MIMEText('send tu','plain','utf-8'))

with open('111.png','rb') as f:
	mime=MIMEBase('image','png',filename='111.png')
	mime.add_header('Content-Disposition','attachment',filename='111.png')
	mime.add_header('Content-id','<0>')
	mime.add_header('X-Attachment-id','0')
	mime.set_payload(f.read())
	encoders.encode_base64(mime)
	msg.attach(mime)

server=smtplib.SMTP(smtp_server,25)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()
#加上附件的发送邮件
#msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
#    '<p><img src="cid:0"></p>' +
#    '</body></html>', 'html', 'utf-8'))
#邮件正文发送图片

#加密传输
#smtp_server = 'smtp.gmail.com'
#smtp_port = 587
#server = smtplib.SMTP(smtp_server, smtp_port)
#server.starttls()