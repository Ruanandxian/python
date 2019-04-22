class Student(object):
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self,value):
        self._birth=value#(可读写）

    @property
    def age(self):
        return 2018-self.birth#(只读）
