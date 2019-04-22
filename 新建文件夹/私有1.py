class Student(object):
    def __init__(self,name,score):
        self.name=name
        self.__score=score
    def get_score(self):
        return self.__score

    def set_score(self,score):
        self.__score=score

