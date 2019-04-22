class Student(object):
    pass


def set_age(self, age):
    self.age = age


b = Student()
b.name = 'gggg'
# 给实例绑定一个方法
from types import MethodType

b.set_age = MethodType(set_age, b)
b.set_age(55)
b.age
# 给类绑定一个方法
Student.set_age = set_age
a = Student()
a.set_age(100)
a.age


# 限制实例的定义
class Month(object):
    __slots__ = ('name', 'age')
