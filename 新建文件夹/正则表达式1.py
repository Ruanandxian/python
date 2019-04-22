import re
m=r'^([a-z.]+)@.com'
n=re.match(m,'mao.mi@.com')
print(n)

l=r'<([a-zA-Z.]+)>([a-z.]+)@.com'
a=re.match(l,'<woai>mao.mi@.com').group(1)
print(a)