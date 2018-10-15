# (A)Python 介紹
## python直譯式的強型別物件導向語言
 註:「強型別」隱含著程式語言對容許混合情況出現加上了嚴格的限制，以避免程式碼以無效的資料使用方式編譯或執行。
 
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

          
## 應用範圍
  *  [iphone mdm](https://youtu.be/G-C-kimmPok?t=47)
  *  web - django / flask
  *  line bot - [django](https://github.com/Lee-W/line_echobot)/[flask](https://github.com/line/line-bot-sdk-python) (訂便當line bot)
  *  desktop - [tkinter](https://github.com/eggeggss/a-face-recognition-wrapper-system) /pyQT
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

***

# (C)變數宣告
  * ### 數值資料型態
   ```sh
  num=10
  print(num)
   ```
   
   ```sh
  num=10.01
  print(num)
   ```
  * ### 布林
  
  ```sh
  flag=True
  print(flag)
  ```
  
  ```sh
  flag=False
  print(flag)
  ```
  
  * ### 字串資料型態
  >>用 " or '表示
  ```sh
  name="Hello world"
  print(name)
  
  name=' "Hello world" '
  print(name)
  
  ```
  >>字串本身就是list組合
  ```sh
  name="Roger"
  print(name[0])
  ```
  
  ```sh
  name="Roger"
  print(name[1])
  ```
  
  >>字串格式化
  ```sh
  age=20
  print('my name is roger ,I am {} years old.'.format(age)) 
  print('my name is roger,I am',age,'years old.')
  ```
  
  
 

This is [an example](http://example.com/ "Title") inline link.
[android](https://dotblogs.com.tw/eggstudio/2017/07/19/085851)

