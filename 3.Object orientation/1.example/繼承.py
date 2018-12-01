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
      pass

class Cat(Animal):
      pass


if __name__=='__main__':
    mydog=Dog()
    mydog.name='big dog'
    mydog.eat()