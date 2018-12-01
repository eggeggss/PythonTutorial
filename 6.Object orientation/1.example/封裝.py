#將name設為private外界無法修改,前面加2個底線

class Animal:

    def __init__(self,name):
        self.name=name

    def eat(self):
        print('動物吃東西')

    def drink(self):
        print('喝水')


class Dog(Animal):
      pass

class Cat(Animal):
      pass


if __name__=='__main__':
    mydog=Dog('big dog')
    print(mydog.name)
    mydog.eat()