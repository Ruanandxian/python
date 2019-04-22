from collections import namedtuple
#nametuple表示坐标
Point=namedtuple('Point',['x','y'])
p=Point(1,3)
print(p.x)
print(p.y)
San=namedtuple('San',['x','y','z'])
m=San(1,2,3)
print(m.x,m.y,m.z)
#deque,适用于队列和栈
from collections import deque
b=deque(['x','y','z'])
b.append('a')#加到末尾
b.appendleft('b')#加到开头
b.pop()#删除末尾
b.popleft()#删除开端
print(b)
#defaultdict#使用dict，如果key不存在，抛出一个默认值
from collections import defaultdict
dd=defaultdict(lambda:'nonono')#默认值函数
dd['key1']=1
print(dd['key1'])
print(dd['key2'])
#OrderedDict
from collections import OrderedDict
mn=[('a',1),('c',3),('b',2)]#key无序
mm=OrderedDict([('a',1),('c',3),('b',2)])#key有序
mm['z']=4
mm['y']=5
print(mm.keys())         #OrderedDict按照插入顺序排序
print(mm)
#Counter计数器
from collections import Counter
c=Counter()
r='galkjdfijxblkcji'
for i in r:
    c[i]=c[i]+1
print(c)
Counter(r)#直接调用计数器