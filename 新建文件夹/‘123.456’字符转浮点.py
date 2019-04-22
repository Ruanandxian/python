from functools import reduce
L={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
def re(s):
    return L[s]

m=list(map(re,'123456'))

def cj(x,y):
    return x*10+y

n=reduce(cj,m)/1000

print(n)