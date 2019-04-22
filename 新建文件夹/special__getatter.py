class Student(object):
    def __init__(self):
        self.name='mmmmm'

    def __getattr__(self,attr):
        if attr=='score':
            return 99
        if attr=='age':
            return lambda:25
        raise AttributeError('\'student\'object has no attribute\'%s\''%attr)

s=Student()
print(s.name)
print(s.score)
print(s.age())
print(s.grade)
