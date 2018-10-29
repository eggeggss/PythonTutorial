
def SumAnyNumber(*args):
    
    total=0
    for item in args:
        total=total+item
    print(total)


def SumThree(number1,number2,number3):
    print(number1+number2+number3)


def SumTwo(number1,number2):
    print (number1+number2)


SumAnyNumber(10,20,30,50,60,79,80)
#SumTwo(10,20)
