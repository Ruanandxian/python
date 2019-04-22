import hashlib
def login(name,password):
    login=hashlib.md5()#md5值e10adc3949ba59abbe56e057f20f883e
    login_1=hashlib.sha1()#sha1的值7c4a8d09ca3762af61e59520943dc26494f8941b
    login.update(password.encode('utf-8'))
    login_1.update(password.encode('utf-8'))
    print(name,login.hexdigest(),login_1.hexdigest())#.hexdigest()得到相应的值

login('micheael','123456')
