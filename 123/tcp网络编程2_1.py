import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',9999))
print(s.recv(1024).decode('utf-8'))
for data in [b'Michael',b'Tracy',b'Sarah']:
	s.send(data)#发送数据
	print(s.recv(1024).decode('utf-8'))
s.send(b'exit')#发送结束的语句
s.close()