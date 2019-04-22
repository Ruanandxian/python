import json
d=dict(name='bbbb',score=88,age=12)
with open('ttt.txt','w') as m:
    json.dumps(d)#返回一个str内容就是标准的JSON
    json.dump(d,m)#把JSON写入一个文件
with open('ttt.txt','r') as c:
    json.loads(c)#反序列化为str
    j=json.load(c)#反序列化到c
#s='{"name": "bbbb", "score": 88, "age": 12}'#str对象
#json.loads(s)#反序列化为对象
#结果{'name': 'bbbb', 'score': 88, 'age': 12}