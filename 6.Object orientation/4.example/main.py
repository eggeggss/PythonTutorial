
class GameRole:

    @staticmethod
    def createRole(type):
        if type=='魔王':
           return 魔王()
        elif type=='戰士':
           return 戰士('狂戰士')
        elif type=='魔法師':
           return 魔法師('超級魔法師')

    def __init__(self,name,hp,hit):
        self.__hp=hp
        self.__hit=hit
        self.__name=name

    def setHp(self,hp):
        self.__hp=hp

    def getHp(self):
        return self.__hp

    def getName(self):
        return self.__name

    #攻擊
    def attack(self,who):
        hp=who.getHp()
        if hp>0:
           hp=hp-self.__hit
           who.setHp(hp)
        else:
           who.setHp(0)
        print('\033[1;33;33m')
        print(self.getName(),'攻擊',who.getName())
        print('\033[0m')

    def checkstatus(self):
        if self.__hp <= 0:
           print('\033[1;30;31m')
           print(self.__name+'已經死亡,請勿鞭屍')
           print('\033[0m')

class 魔王(GameRole):

    def __init__(self):
        super().__init__('巴哈姆特',1000,100)
        print('大魔王出現了~~')


class 戰士(GameRole):

    def __init__(self,name):
        super().__init__(name,500,10)
        print('新增一位戰士~~')


class 魔法師(GameRole):

    def __init__(self,name):
        super().__init__(name,400,100)
        print('新增一位戰士~~')



if __name__=='__main__':

    #read roles from config
    m1=GameRole.createRole('魔王')
    w1=GameRole.createRole('戰士')
    r1=GameRole.createRole('魔法師')
    '''
    m1=魔王()
    w1=戰士('狂戰士')
    r1=魔法師('超級魔法師')
    '''

    while True:
        number = int(input('1:劍士功擊/2:魔法師功擊=> 你要做什麼？'))
        if number == 1:
            w1.attack(m1)
        elif number == 2:
            r1.attack(m1)
        else:
            print('不知道你要幹嘛')
            continue

        print('魔王的血剩下',m1.getHp())
        #確認魔王狀態
        m1.checkstatus()
