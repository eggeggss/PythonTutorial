# (D)流程控制
```sh
   
   if (條件1):
      do..something
   elif (條件2):
      do..something
   else :
      do..something
      
```

# (E)迴圈
```sh
#印出1~9
for i in range(1,10):
   print(i)

#1~100跳2個印
#range(起始,結束-1,間隔)
for i in range(1:101:2):
    print(i)

#while回圈
while (True):
   do...something
   if (條件一):
      break
   else :
      continue

```

## 練習
讓使用者輸入成績,成績在90以上就顯示優等,
80~89顯示甲等,70~79顯示乙等,60~69顯示丙,60以下丁
```sh

while True:
   score=int(input('請輸入成績,輸入-1結束'))

   if(score>=90):
        print('優等')
   elif(score>=80):
        print('乙等')
   elif(score>=70):
        print('丙等')
   elif(score>0):
        print('丁等')
   else:
       break
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


#自定義函式+預設值
#一開始有預設值,後面參數都要加預設值
def Sum(a=10,b=1)
    print(a+b)
  
#不按參數順序呼叫,必須使用參數名稱=值
Sum(b=2)

```
# (G)模組與套件
  * ㄧ個.py檔案就是一個模組
  * python 運作的基礎,可以想像組點腦的驅動程式,每一個模組都如同一個驅動程式
  * 為何需要模組 - 把定義或需要執行的程式已照功能分門別類,易於管理(關注點分離)
  * 使用方法 - import 模組名稱
  
  * 套件(package)就是一堆模組(py)的集合,通常會把相似功能的模組收入一個套件
  * from 模組 import 函式或變數


# (H)檔案

# (I)資料庫

# (J)物件導向
    ## 繼承
    ## 多型
    ## 封裝
    

    
