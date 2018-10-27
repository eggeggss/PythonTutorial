# (D)流程控制
```sh
   
   if (條件1):
      do..something
   elif (條件2):
      do..something
   else:
      do..something
      
```

# (E)迴圈
```sh
#印出1~9
for i in range(1,10):
   print(i)

#跳2個印
nlist=range(1,101):

for i in nlist[::2]:
    print(i)

#while回圈
while (True):
   do...something
   if (條件一):
      break
   else:
      continue

```
# (F)函數
要先有def以後才可以開始使用
```sh

#2個參數相加
def addTwoNumber(number1,number2):
    return number+number2

#不定參數相加 (*是陣列)
def addAnyNumber(*arg):
    total=0
    for number in arg:
        total=total+number
    return total
    
addAnyNumber(1,2,3,4,5,6,7...)


#不定參數用法2(**是dictionary)
def calculateScore(**kwarg):
    print('英文成績是:',kwarg['english'])
    print('數學成績是:',kwarg['math'])

calculateScore(math=100,english=90)

```
# (G)模塊

# (H)物件導向
    ##繼承
    ##多型
    ##封裝

