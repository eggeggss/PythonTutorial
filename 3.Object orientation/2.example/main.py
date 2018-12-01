
魔王hp=100
戰士hp=100
魔法師hp=100

def 處理扣血(扣血):
    global 魔王hp
    if 魔王hp<=0:
       print('\033[1;30;31m')
       print('魔王已經死亡,請勿鞭屍')
       print('\033[0m')
    else:
       魔王hp=魔王hp-扣血

def 劍士攻擊():
    處理扣血(1)
    print('用劍攻擊魔王')

def 魔法師攻擊():
    處理扣血(10)
    print('用魔法攻擊魔王')

def 確認魔王的血():
    global 魔王hp
    print('魔王的血剩：',魔王hp)
    if 魔王hp<0:
       print('魔王被打倒')

def 劍士補血():
    pass

if __name__=='__main__':

    while True:
        number=int(input('0:劍士功擊/1:魔法師功擊=> 你要做什麼？'))

        if number==0:
           劍士攻擊()
        elif number==1:
           魔法師攻擊()

        確認魔王的血()