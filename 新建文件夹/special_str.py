class Student(object):
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return 'wosi%s'%self.name
    __repr__=__str__