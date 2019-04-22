#from io import BytesIO
#d=BytesIO()
#d.write('中文'.encode('utf-8'))
#d.getvalue()

from io import BytesIO
d=BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(d.read())
