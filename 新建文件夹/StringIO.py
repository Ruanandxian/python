#from io import StringIO
#f=StringIO()
#f.write('hello')
#f.write(' ')
#f.write('world')

from io import StringIO
f=StringIO('hello\n  \nword\n')
while True:
    s=f.readline()
    if s=='':
        break
    print(s.strip())