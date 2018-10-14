# (A)Python 介紹
## python直譯式的物件導向語言
 [Python 2.0](http://shopping.pchome.com.tw)於2000年10月16日發布，增加了實現完整的垃圾回收，並且支援Unicode。同時，整個開發過程更加透明，社群對開發進度的影響逐漸擴大。
 
 Python 3.0於2008年12月3日發布，此版不完全相容之前的Python原始碼。不過，很多新特性後來也被移植到舊的Python 2.6/2.7版本。

 ### 優點
 * 快速開發,適合小型專案
 * library多
 * open source
 * 豐富的科學分析package ex.numpy,scipy,matplotlib,axes3d
 * 跨平台 - windows,linux,osx,[android](https://dotblogs.com.tw/eggstudio/2017/07/19/085851) 
 * 膠水語言-易與其他語言介接-cpython/jython/IRONpython
 ### 缺點                  
 * [效能差](https://www.cnblogs.com/savorboard/p/dotnet-benchmarks.html) [?](http://python.jobbole.com/87814/)
 * runtime error (型別檢查)
 * GIL(使用 GIL 的解釋器也只允許同一時間執行一個執行緒)

          
## 應用範圍
  *  [iphone mdm](https://youtu.be/G-C-kimmPok?t=47)
  *  web - django / flask
  *  desktop - tkinter /pyQT
  *  web crawler - selenium / beatifulsoup + requests
  *  raspberry pi - [opencv](https://www.facebook.com/100009153019778/videos/2101438776837869/)
  *  machine learning/deep learning - scikit-learn / tensortflow / keras /pytorch
  *  bot - [line bot](https://github.com/line/line-bot-sdk-python)/telegram
  *  車牌辨識 - [openalpr](https://github.com/openalpr/openalpr)
  

***

# (B)環境設定
## 1.安裝Python3
  * ### [python3.6](https://www.python.org/downloads/release/python-362/)
  
  * ### 設定環境變數
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
  activative
  
  ```
  
  (mac/linux)
  ```sh
  
  source ./env/activative
  ```
This is [an example](http://example.com/ "Title") inline link.
[android](https://dotblogs.com.tw/eggstudio/2017/07/19/085851)
