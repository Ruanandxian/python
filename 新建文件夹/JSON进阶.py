import json
class Student(object):
    def __init__(self,name,score,age):
        self.name=name
        self.score=score
        self.age=age

def dict(d):
    return Student(d['name'],d['age'],d['score'])
d=Student('bbbb',55,18)
m=json.dumps(d,default=lambda obj:obj.__dict__)#将类序列化
print(json.loads(m,object_hook=dict))#反序列化对象，