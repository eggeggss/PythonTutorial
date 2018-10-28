# (A)Python 介紹
## python直譯式的強型別物件導向語言
 
 ### 何謂強型別
 wiki定義「強型別」隱含著程式語言對容許混合情況出現加上了嚴格的限制，以避免程式碼以無效的資料使用方式編譯或執行。(廣義)
 
 will保哥的定義 強型別是一種觀念，是指「盡量使用具有型別的方式開發」，這樣的開發方式可以讓開發人員在「編譯時期(Compile-Time)」就能夠發現錯誤，
 減少「執行時期(Runtime)」發生錯誤的機會(狹義)
 
 ### python歷史
 
 1989年的聖誕節期間，吉多·范羅蘇姆為了在阿姆斯特丹打發時間，決心開發一個新的指令碼解釋程式，繼承自ABC語言
 
 [Python 2.0](https://pythonclock.org)於2000年10月16日發布，增加了實現完整的垃圾回收，並且支援Unicode。同時，整個開發過程更加透明，社群對開發進度的影響逐漸擴大。
 
 Python 3.0於2008年12月3日發布，此版不完全相容之前的Python原始碼。不過，很多新特性後來也被移植到舊的Python 2.6/2.7版本。

 * ### 優點
 > * 快速開發,適合小型專案
 > * library多
 > * open source
 > * 豐富的科學分析package ex.numpy,scipy,matplotlib,axes3d
 > * 跨平台 - windows,linux,osx,[android](https://dotblogs.com.tw/eggstudio/2017/07/19/085851) 
 > * 膠水語言-易與其他語言介接-cpython/jython/IRONpython
 * ### 缺點                  
 > * [效能差](https://www.cnblogs.com/savorboard/p/dotnet-benchmarks.html) [?](http://python.jobbole.com/87814/)
 > * runtime error (型別檢查)
 > * GIL(使用 GIL 的解釋器也只允許同一時間執行一個執行緒)
        所有在直譯器中的 C 程式碼都必須要在執行 Python 時握著這把鎖。
        作者首先以這種方式建構 Python，因為它很簡單。
        並且，每次從 CPython 移除 GIL的嘗試都讓單執行緒的程式碼效能降低，而無法從多執行緒中獲益。
        GIL 對程式所造成的影響簡單到你可以在手背上寫下這個原則：「當有一個執行緒在執行 Python，其他 N 個執行緒都在睡覺或是等待 I/O」。

          
## 應用範圍
  *  [iphone mdm](https://youtu.be/G-C-kimmPok?t=47)
  *  web - django / flask
  *  line bot - [django](https://github.com/Lee-W/line_echobot)/[flask](https://github.com/line/line-bot-sdk-python) (訂便當line bot)
  *  desktop - tkinter /pyQT
  *  web crawler - selenium / [beatifulsoup+requests](https://dotblogs.com.tw/eggstudio/2017/12/28/python1)
  *  raspberry pi - [opencv](https://www.facebook.com/100009153019778/videos/2101438776837869/)
  *  車牌辨識 - [openalpr](https://github.com/openalpr/openalpr)
  *  大數據分析 -  Spark 分散式處理巨量資料，加速分析流程，縮短 AI 訓練的時間.
  *  machine learning/deep learning - scikit-learn / tensortflow / keras /pytorch
  
***

# (B)環境設定
## 1.安裝Python3
  * ### [python3.6](https://www.python.org/downloads/release/python-362/)
  
  * ### 設定環境變數(Windows)
```sh      
 C:\Users\luffymchd888\AppData\Local\Programs\Python\Python36;
 C:\Users\luffymchd888\AppData\Local\Programs\Python\Python36\Scripts;
```
  * ### 下載 [visual studio code](https://code.visualstudio.com/download)

## 2.設定虛擬環境 
  (目的使不同專案的環境在同一個作業系統上不互相干擾)
  * ### 安裝virtualenv
 
 ```sh
  pip3 install virtualenv env
  ```
  * ### 創建虛擬環境
  ```sh
  python3 -m virutalenv env 
  ```
  
  * ### 執行虛擬環境
  
  (windows)
  ```sh
  
  cd env\Scripts\
  activate
  
  ```
  
  (mac/linux)
  ```sh
  
  source ./env/activate
  ```


  * ### python的規定
  單行註解使用#
  多行註解使用'''

  使用縮排當作程式碼區塊

***

  
# 運算式

 ![alt tag](https://github.com/eggeggss/PythonTutorial/blob/master/算術運算子.png?raw=true)
  

 ![alt tag](https://github.com/eggeggss/PythonTutorial/blob/master/關係運算子.png?raw=true)
  
  
 ![alt tag](https://github.com/eggeggss/PythonTutorial/blob/master/邏輯運算子.png?raw=true)
  

# (C)變數宣告
  ![alt tag](https://github.com/eggeggss/PythonTutorial/blob/master/immutable.png?raw=true)
  
  * ## 數值資料型態
  
  * ### Integer
  
   ```sh
  num=10
   ```
  * ### float 小數(不精確)   
   ```sh
  num=10.01
   ```
  * ### Decimal 小數(精確,速度慢)
  
  ```sh
   c=0.3
   d=0.9
   c*3==d
   >>>>False
  
   import decimal
   a=decimal.Decimal('0.3')
   b=decimal.Decimal('0.9')
   a*3==d
   >>>>True
  ```
  
  * ### 布林
  
  ```sh
  flag=True
  
  flag=False
  ```
  
  
  * ### 字串資料型態
  >>一連串單字組成,用 " or '表示
  ```sh
  name="Hello world"
 
  name=' "Hello world" '
 
  
  ```
  >>字串本身就是list組合
  ```sh
  name="Roger"
  name[0]
  
  
  #判斷字串字串是否為數字
    a="123"
    b="abc" 
    a.isdigit()
    b.isdigit()
  ```
  
  ```sh
    #判斷前幾個字是否為abc
    s1="abcdedf"
    s1.startswith("abc")
  
  ```
  
  
  >>字串格式化
  ```sh
  
  age=20
  
  name="roger"
  
  print('my name is {} ,I am {} years old.'.format(name,age)) 
  
  print('my name is roger,I am',age,'years old.')
  ```

  * ## 群集資料型態
  
  ```sh
  list  [] 
  
  tuple  ()  
  
  set  {"a","b"} 
  
  dictionary {"a":1,"b":2} 
  
  ```
  
  * ### List (串列)
  list are mutable sequences,可放不同型態的物件,但建議放相同型態物件
  ```sh
  mylist=list()
  mylist=['A','B',1]
  
  #設值
  mylist.append('C')
  
  #取出最後一個值,該值從陣列消失
  mylist.pop()
  
  #取出第一個值,該值從陣列消失
  mylist.pop(0)
  
  #排序
  mylist.sort()
  
  #陣列反轉
  mylist.reverse()
  
  #印前面2個元素
  mylist[:2]
  
  #印陣列第2到最後
  mylist[2:]
  
  #印倒數2個元素
  mylist[-2:]
  
  ```
  
  練習
  設計一個成績輸入的程式,學生成績輸入串列元素,如果輸入-1程式結束,並顯示總成績與平均
  
  ```sh
  score=[]
  total=inscore=0
  while (inscore !=-1):
      inscore=int(input("請輸入成績:"))
      score.append(inscore)
      
  for i in score:
     total=total+1
  
  average=total/ (len(score)-1)
  
  print('總成績:{} , 平均 {}',total,average)
  
  ```
  
  * ### Tuple (元組)
  與List一樣,差異是immutable,只能取資料
  優點效率好,保護資料
  
  ```sh
  #設值
  mytuple=('A','B',1)
  
  #取值
  mytuple[0]
  
  ```
  
  * ### Set (集合)
  不重複的集合
  ```sh
  s=set()
  
  s.add("A") #新增一集合
  
  s.discard("A") #刪除某元素 不會throw error
  
  s.remove("A")  #刪除某元素 不存在會throw error
  
  s.union(t) 聯集2個set
  
  s.intersection(t)
  
  ```
  
  * ### Dictionary (字典)
  由一組匹配的key跟value所組成的集合
  ```sh
 
  mydict=dic()
  #直接設值
  mydict={'name':'John','age':20,}
  
  #設值
  mydic["name"]="John"
  
  #取值,若找不到會throw error
  name=mydic["name"]
  
  #取值,若找不到會回傳None
  name=mydic.get("name")
  
  #將key轉成list
  mydictkeys=list(mydic.keys())
  mydictvalues=list(mydic.values())
 
  #清除字典
  mydic.clear()

  #印出字典內容
  for key,value in mydic.items():
      print("key:",key,"value:",value)

 
  ```

