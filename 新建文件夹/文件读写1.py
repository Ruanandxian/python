#f=open('C:/Users/Administrator/test.jpg','r',encoding='utf-8',errors='ignore')
#f=open('C:/Users/Administrator/abc.txt','r+')#读写文件
#a追加到文件末尾
#w写文件
#r读文件
with open('C:/Users/Administrator/test.txt','r+') as f:
    f.write('hello word')
