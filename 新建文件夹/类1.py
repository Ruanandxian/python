class Student(object):
    def __init__(self,name):
        self.name=name

    def grade(self):
        if self.name>90:
            print('a')
        else:print('b')
b=Student(78)
b.grade()
