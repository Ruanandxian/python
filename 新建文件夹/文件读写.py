#f=open('C:/Users/Administrator/test.txt','r')
#with open('C:/Users/Administrator/test.txt','r') as f:
#   print(f.read())
d=open('C:/Users/Administrator/test.txt','r')
for x in d.readlines():
    print(x.strip())#去除\n
d.readline()#读一行
d.readlines()#全部读完，返回list
d.read(size)#读取指定的字节

