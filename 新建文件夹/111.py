import hashlib

login = hashlib.sha1()
login.update('hello'.encode('utf-8'))
print(login.hexdigest())
