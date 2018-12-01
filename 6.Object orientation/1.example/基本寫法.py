
class Dog:

    #欄位
    name='大寶'

    #建構子
    def __init__(self):
        print('一隻狗被產生')

    #方法
    def eat(self):
        print('吃東西')



class Cat:

    def eat(self):
        print('吃東西')

if __name__=='__main__':
    mydog=Dog()
    mydog.eat()
    print(mydog.name)

    mycat=Cat()
    mycat.eat()

