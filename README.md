# (A)Python 介紹
## python直譯式的物件導向語言
 ### 優點
 * 快速開發,適合小型專案
 * library多
 * 跨平台 - windows,linux,osx,[android](https://dotblogs.com.tw/eggstudio/2017/07/19/085851) 
 * 膠水語言-易與其他語言介接-cpython/jython/IRONpython
 ### 缺點                  
 * [效能差](https://www.cnblogs.com/savorboard/p/dotnet-benchmarks.html)
 * runtime error (no 型別檢查)
 * 不適合用於大型專案
 * GIL(使用 GIL 的解釋器也只允許同一時間執行一個執行緒)

          
## 應用範圍
  *  web - django / flask
  *  desktop - tkinter /pyQT
  *  web crawler - selenium / beatifulsoup + requests
  *  raspberry pi - [opencv](https://www.facebook.com/100009153019778/videos/2101438776837869/)
  *  machine learning/deep learning - scikit-learn / tensortflow / keras /pytorch
  *  bot - [line bot](https://github.com/line/line-bot-sdk-python)/telegram
  *  [iphone mdm](https://github.com/project-imas/mdm-server)
  *  車牌辨識 - [openalpr](https://github.com/openalpr/openalpr)
  

***

# (B)環境設定
## 1.安裝Python3
  * ### python3.6(https://www.python.org/downloads/release/python-362/)
  
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
