import itertools
def Pi(s):
    a=itertools.count(1,2)
    b=list(itertools.takewhile(lambda x:x<2*s,a))
    flag = 0
    sum = 0
    for n in b:
        if flag==0:
            sum+=4/n
            flag=1
        else:
            sum+=-4/n
            flag=0

    return sum

print(Pi(10000))

natuals=itertools.count(1,3)
#for i in natuals:
#    print(i)
# 无限的跑下去，1开始，3间隔

cs=itertools.cycle('adc')
#for c in cs:
#   print(c)
#无限的跑下去，abc循环

ns=itertools.repeat('a',3)
#for n in ns:
#   print(n)
#跑指定的次数

mm=itertools.count(1)
sb=list(itertools.takewhile(lambda x:x<=10,mm))
print(sb)
#跑自定义的匿名函数

for c in itertools.chain('adc','bbb'):
    print(c)
#两个串联跑，一次

for key,group in itertools.groupby('AAAaaadfbbbdcccc',lambda x:x.upper()):
    print(key,list(group))
#把迭代器中相邻的重复元素挑出来放在一起
#实际挑选规则是通过函数完成的，可以自定义匿名函数

