from wsgiref.simple_server import make_server
from hello import application
httpd=make_server('',8200,application)
print('Serving Http on port 8200...')
httpd.serve_forever()