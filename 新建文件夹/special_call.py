class Student(object):
    def __init__(self,name):
        self.name=name

    def __call__(self):
        print('woai%s'%self.name)

a=Student('nnnn')
a()