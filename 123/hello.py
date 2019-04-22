'''def application(environ,start_response):
	start_response('200 OK',[('Content-Type','text/html')])
	return [b'<hl>Hellow,web!</hl>']'''


def application(environ,start_response):
	start_response('200 OK',[('Content-Type','text/html')])
	body='<hl>hello,%s!</hl>'%(environ['PATH_INFO'][1:]or'web')
	return [body.encode('utf-8')]