# (D)流程控制
```sh
   
   if (條件1):
      do..something
   elif (條件2):
      do..something
   else :
      do..something
      
```

## 練習
讓使用者輸入成績,成績在90以上就顯示優等,
80~89顯示甲等,70~79顯示乙等,60~69顯示丙,60以下丁
```sh


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

# (H)檔案

# (I)資料庫

# (J)物件導向
    ## 繼承
    ## 多型
    ## 封裝
    
# (K)爬蟲

    
