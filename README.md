# Python 介紹
## python直譯式的物件導向語言

* ### 優點
           1.快速開發
           2.library多
           3.跨平台
           4.膠水語言-易與其他語言介接-cpython/jython/IRONpython
          
* ### 缺點
          1.效能差
          2.runtime error
          3.GIL(使用 GIL 的解釋器也只允許同一時間執行一個執行緒)



***

# 環境設定
## 1.安裝Python3
  * ### python3.6(https://www.python.org/downloads/release/python-362/)
  
  * ### 設定環境變數
```sh      
 C:\Users\luffymchd888\AppData\Local\Programs\Python\Python36;
 C:\Users\luffymchd888\AppData\Local\Programs\Python\Python36\Scripts;
```
  
## 2.設定虛擬環境
  * ### 安裝virtualenv
 
 ```sh
  pip3 install virtualenv env
  ```
  * ### 創建虛擬環境
  ```sh
  python3 -m virutalenv env 
  ```
  
  * ### 執行虛擬環境
  ```sh
  cd env\Scripts\
  activative
  ```
This is [an example](http://example.com/ "Title") inline link.
