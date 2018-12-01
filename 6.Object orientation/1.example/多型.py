#用抽象化將一樣的特徵移至super class

class Animal:
    name=''
    def __init__(self):
        pass

    def eat(self):
        print('動物吃東西')

    def drink(self):
        print('喝水')


class Dog(Animal):

    def eat(self):
        print('用狗的方式吃')

class Cat(Animal):
      pass


if __name__=='__main__':
    animals=[Dog(),Cat()]

    for animal in animals:
        animal.eat()
