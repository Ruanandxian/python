import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('www.4399.com.cn',80))
s.send(b'GET /HTTP/1.1\r\nHOST:www.4399.com.cn\r\nConnection:close\r\n\r\n')
buffer=[]#接收数据
while True:
	d=s.recv(1024)
	if d:
		buffer.append(d)
	else:
		break
data=b''.join(buffer)
s.close()#关闭连接

#分离http头和文件
header,html=data.split(b'\r\n\r\n',1)
print(header.decode('utf-8'))
with open('bai.html','wb') as f:
	f.write(html)