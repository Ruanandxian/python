import socket
import threading
import time
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',9999))#监听地址和端口
s.listen(5)#开始监听
print('waiting for connection...')
def tcplink(sock,addr):
	print('Accept new connection form %s:%s...'%addr)
	sock.send(b'welcome!')
	while True:
		data=sock.recv(1024)
		time.sleep(1)
		if not data or data.decode('utf-8')=='exit':
			break
		sock.send(('hello,%s!'%data.decode('utf-8')).encode('utf-8'))
	sock.close()
	print('connection from %s:%s'%addr)
while True:
	sock,addr = s.accept()  # 接收一个连接
	# 创建一个新的线程用来处理TCP连接
	t = threading.Thread(target=tcplink,args=(sock,addr))
	t.start()
