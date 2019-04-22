def fn(self,name='mmmm'):
    print('name%s'%name)

Hello=type('Hello',(object,),dict(hello=fn))
#type创建一个class
#type()
#1.class 的名称
#2.继承的父类，只有一个父类，单元素加个逗号
#3.class的方法名称与函数绑定，这里把fn绑定到hello上