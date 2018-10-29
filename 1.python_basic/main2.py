
def determineLevel(score):
    if inscore>=90:
        print('優等')
    elif inscore>=80:
        print('甲等')
    elif inscore>=70:
        print('乙等')
    elif inscore>=60:
        print('丙等')
    elif inscore>=0:
        print('丁等') 

inscore=0

while (True):
    
    inscore=input('請輸入成績:')
    
    if inscore=='-1':
        break

    if (inscore.isdigit())==False:
        print('請輸入數字')
        continue
    else:
        inscore=int(inscore)
        determineLevel(inscore)
        