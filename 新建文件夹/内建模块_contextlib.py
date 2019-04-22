from contextlib import contextmanager
from contextlib import closing
from urllib.request import urlopen
class Query(object):
    def __init__(self,name):
        self.name=name
    def query(self):
        print('Query info aobut %s..'%self.name)

@contextmanager
def create_query(name):
    print('Begin')
    q=Query(name)
    yield q
    print('end')

with create_query('bab') as q:
    q.query()

@contextmanager
def tag(name):
    print('<%s>'%name)
    yield
    print('</%s>'%name)

with tag('h1'):
    print('hello')
    print('world')

with closing(urlopen('http://www.hrxy.com')) as page:
    for line in page:
        print(line)