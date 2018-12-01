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
80 ~ 89顯示甲等,70 ~ 79顯示乙等,60 ~ 69顯示丙,60以下丁
```sh

while True:
   score=int(input('請輸入成績,輸入-1結束'))

   if(score>=90):
        print('優等')
   elif(score>=80):
        p:rint('乙等')
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


addAnyNumber(1,2,3,4,5,6,7)


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
  
  參考5.python_module範例
  
# (I)物件導向

  ## 定義
  ```sh
  指一種程序設計範型，同時也是一種程序開發的方法。用物件的方式來思考與設計系統
  ```

  ## 目的
  ```sh
  重複使用程式碼,提高系統內聚力降低耦合力
  ```
  
  ## 須符合物件導向6大原則solid
  
  單一職責(SRP):一個類別只負責一件事情
  
  開放封閉(OCP):關閉修改,開放擴充
  
  里氏替換(LSP):子類別應該可以替換掉父類別而不會影響程式架構。
  
  介面隔離(ISP):把不同功能的功能從介面中分離出來。
  
  倚賴反轉(DIP):細節依賴在抽象概念。
  
  ## 3大精神
  * 繼承
```sh
   
    在某種情況下，一個類別會有「子類別」。子類別比原本的類別(稱為父類別)要更加具體化，
    也就是說子類別繼承了父類別。例如：計程車(子類別)繼承了汽車(父類別)原有的屬性以及方法，
    也新增了自己特有的屬性(driverName)。
    
```

  * 封裝
  
```sh
   封裝是通過限制只有特定類別的物件可以存取這一特定類別的成員，而它們通常利用介面實作訊息的傳入傳出。
```
  
  * 多型

```sh
    是指由繼承而產生的相關的不同的類別，其物件對同一訊息會做出不同的回應
```

    
