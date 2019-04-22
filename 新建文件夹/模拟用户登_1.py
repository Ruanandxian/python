import hashlib,hmac
message=b'hello world'#.encode可以改变编码
key=b'ruan'#传入的都是bytes
mm=hmac.new(key,message,digestmod='md5').hexdigest()#为md5值加盐

def get_hmac(password,key):
    return hmac.new(key.encode('utf-8'),password.encode('utf-8'),digestmod='md5').hexdigest()

class User(object):
    def __init__(self,name,password):
        self.name=name
        self.key='ruan'
        self.password=get_hmac(password,self.key)

db={
    'michael':User('michael','123456'),
    'bob':User('bob','abc999')
}

def login(name,password):
    user=db[name]
    return user.password==get_hmac(password,'ruan')