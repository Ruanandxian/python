import pickle
d=dict(name='bob',age=20,score=88)
pickle.dumps(d)#把任意对象序列化为bytes
f=open('test.txt','wb')#写bytes
pickle.dump(d,f)#将序列化后的d写入f中
f.close()#关闭
f=open('test.txt','rb')#读bytes
b=pickle.load(f)#反序列化对象到b
f.close()#关闭
b#得到对象