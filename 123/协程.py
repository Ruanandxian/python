def consumer():
	r = ''
	while True:
		n = yield r
		if not n:
			return n
		print('[CONSUMER]%s...' % n)
		r = '200 ok'


def produce(c):
	# 首先send       c.send(None)必须发送一个None给consumer
	c.send(None)
	n = 0
	while n < 5:
		n = n + 1
		print('[PRODUCER]Producing %s...' % n)
		r = c.send(n)#将n传入consumer函数，同时yield r=n=consumer的n
		#执行到第二次循环的yield返回produce，打印此时r的字符
		print('[PRODUCER]Consumer return %s' % r)
		#循环
	c.close()


c = consumer()
produce(c)
#执行中间两个函数间来回跳转