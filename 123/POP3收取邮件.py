# 第一步：用poplib把邮件的原始文本下载到本地；
# 第二部：用email解析原始文本，还原为邮件对象。

# 邮箱：1204628226@qq.com
# 密码：yffznttnyntejbhb

from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr
import poplib

email = input('邮箱：')
password = input('密码：')
pop3_server = input('pop3_server:')

# 连接pop3服务器,pop加密，需要ssl
server = poplib.POP3_SSL(pop3_server)

# 打印欢迎用语
print(server.getwelcome().decode('utf-8'))

# 身份认证
server.user(email)
server.pass_(password)

# stat()返回邮件数量和占用的空间
print('Messages:%s.Size:%s' % server.stat())

# list()返回所有邮件的编号
resp, mails, octets = server.list()
print(mails)

# 获取最新的一封邮件
index = len(mails)
resp, lines, octets = server.retr(index)

# lines存储了邮件原始文本的每一行
# 可以获得邮件的原始文本
msg_content = b'\r\n'.join(lines).decode('utf-8')
msg = Parser().parsestr(msg_content)  # 将邮件内容解析为Message对象


# 可以根据邮件索引号直接从服务器删除邮件:
# server.dele(index)
# 关闭连接:


# server.quit()

# 解析邮件
# indent用于缩进显示
def print_info(msg, indent=0):
	if indent == 0:
		for header in ['From', 'To', 'Subject']:
			value = msg.get(header, '')
			if value:
				if header == 'Subject':
					value = decode_str(value)
				else:
					hdr, addr = parseaddr(value)
					name = decode_str(hdr)
					value = u'%s <%s>' % (name, addr)
			print('%s%s:%s' % ('  ' * indent, header, value))
	if (msg.is_multipart()):
		parts = msg.get_payload()
		for n, part in enumerate(parts):
			print('%spart %s' % ('	' * indent, n))
			print('%s-------------------------' % ('	' * indent))
			print_info(part, indent + 1)
	else:
		content_type = msg.get_content_type()
		if content_type == 'text/plain' or content_type == 'text/html':
			content = msg.get_payload(decode=True)
			charset = guess_charset(msg)
			if charset:
				content = content.decode(charset)
			print('%sText: %s' % ('  ' * indent, content + '...'))
		else:
			print('%sAttachment:  %s' % ('	' * indent, content_type))


def decode_str(s):
	value, charset = decode_header(s)[0]
	if charset:
		value = value.decode(charset)
	return value


def guess_charset(msg):
	charset = msg.get_charset()
	if charset is None:
		content_type = msg.get('Content-Type', '').lower()
		pos = content_type.find('charset=')
		if pos >= 0:
			charset = content_type[pos + 8:].strip()
	return charset


print_info(msg)
