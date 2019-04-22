class Animal(object):
    def run(self):
        print('paopaopao')


class dog(Animal):
    def he(self):
        print('qweeeeeee')


class cat(Animal):
    def run(self):
        print('ccccccccc')

def run_twice(Animal):
    Animal.run()
    Animal.run()
