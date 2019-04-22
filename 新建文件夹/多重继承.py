class D(object):
    def f(self):
        print('d')
class E(object):
    pass
class F(object):
    def c(self):
        print('f')
class C(D,F):
    pass
class B(E,D):
    pass
class A(B,C):#具备所有属性
    pass
a=A()
#子类覆盖重复父类
print(a.f())