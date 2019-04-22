class Student(object):
    @property
    def score(self):
        return self._score


    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('default')
        if value<0 or value>999:
            raise ValueError('chongxin')
        self._score=value

