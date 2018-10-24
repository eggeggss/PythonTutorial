import requests
import pandas as pd
import time
import matplotlib.pyplot as plt
import numpy as np

url='http://www.taiwanlottery.com.tw/Lotto/Lotto649/history.aspx'
viewstate='bzeO9Oad7ZBLNxAXFPD3LVkUSfI7OIMTK61KdGWEq7spq+OvMoBfk8UjU3IaRAi94m9VKpHpSMByOb8uRF9Y8TuMqwiA9IzjQCk1NnjXap6q6ZS9DeYBV9d+lqUfsr1UwVS1e5BeBGVPBhNiwN3Be5Rd8WtMNO6Z2O3k0UzVpVRkPBtR/c7EojGQAkv7RfvWMMj53VKOJcdKeaNeuXSZZFhPZMsfza4OYYQl7qxPslLBWwu9nHqoDsZWqtaHcgvUXcSBOXRy/cosnrbSLrUFJOJ/WeU52/JL7UjnVrvIlYt2TG3MPphcYlN7U2lfUVgzrkNM3x5HFmpFQfnBvLpOJp6ua2Q5tg5fJlKZUwHgeNBeyRzdoGe6HrAIUNn8kiwfbaH2W9pcCcPnXgdEP8+7Ynan81Ln2rzsiOi8C7Mxy5XQBN5m2SS4yKhwBRP2shKnC5BWU/wdhDtaTMH7bUfhWYskxjQuPL4XpfP7n1rx6wORECT5k9jpy9+vYa9kjyknX9gywVpp9ICfEiBJRk70pT9umVg='
EVENTVALIDATION='J+hKMbJEsBouwekTtYM6BSD3WzwxyEgZEDGTPoN6z01sEjXgNmz1wKFcO/+NJPJERw8fPtfy9laHvaK70pzNDwcb1mo0JXqOMvvdk2ndPgqf0ma7Ld0cbOFRI3WSoIrCfU+GpkT4m2710kTIAZATwX/4JqEe3Kg4JVHIxBSjTeCgIdRAFjP4q9wKYEkDGaclMAoDaXmeWOm6v7Hooa6MY/knPksXlZAcHnGNlHqtmGmd2WJ3guzfOxiXKpY0aBXsVB+VkYT6+FQQwIcS0BlkfX+ldIJpALFKcsrEJHsGZj3Be7e+9LgOKmrrQUq+nnd2O3HPfhsO217AT6/mE3TjR6F1jfa8vH+WG9GbFK/w6S5EBQJ+Qiab3/t+O2QC5Gswno3D3peUGWLavYPXpY39lkbZ6lkicknM7xfesB4kaDrCw6ch1MlfpJyRxYLzrYqbEJIRG3f01qDpytSaEynMtAoR9YuZrU/BzNFrw//Zrvat7ysgyFJNftErjZ60md2ExCvhjRnPfkbc1FSQbeZxGWPIKgzkILiXmu/U+T3oJ/5KMiYpWrTo8pjR+KIRSrNLjNndR5KMdPe/Rfytsv0LWHDvFYXk598sjPWuExa/RMEFBrSDqnX01NdU8P2gezily5l2gAvOSjbexwnCWDiPDvfvkVU2jyZo3vxNPE/8udUYn+Fcr/pMBpjnNGvLpHe1CXN0CKXPr7oqpUKeL+qE9g0d1skBcnvOd5fKzcgVvy9VhH9Hpk6b3oa/3SRBDy0OK5KpKQckBz9/ebj9mEMktkkOpFDPOd1J69KVZNmBVyNjWXT8L07Q5nhCJ3WsdqH2dk6UXA=='

loto_range=['01','02','03','04','05','06','07','08',\
            '09','10','11','12','13','14','15','16',\
            '17','18','19','20','21','22','23',\
            '24','25','26','27','28','29','30','31',\
            '32','33','34','35','36','37',\
            '38','39','40','41','42','43',\
            '44','45','46','47','48','49']

def Initial():
    global group_dict
    group_dict=dict()
    for basenumber in loto_range:
        group_dict[basenumber]=0


def ExcuteCrawler(year,month):
    global url
    
    headers=requests.utils.default_headers()

    headers.update({
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding':	'gzip, deflate',
        'Accept-Language':	'zh-TW,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Cache-Control':'no-cache',
        'Connection':'keep-alive',
        'Content-Length':'8819',
        'Content-Type':'application/x-www-form-urlencoded',
        'Cookie':'ASPSESSIONIDSSRTARDD=HPAMHOPBLHKHEMGJODLMJGNN; ASPSESSIONIDASATTRTQ=PELLGBGDJJKJOOMCPBAIHKFG; ASPSESSIONIDQADBADCD=IDCGNAHDALIGKPCIKCEPKKFH',
        'Host':	'www.taiwanlottery.com.tw',
        'Pragma':	'no-cache',
        'Referer':	'http://www.taiwanlottery.com.tw/Lotto/Lotto649/history.aspx',
        'Upgrade-Insecure-Requests':	'1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:62.0) Gecko/20100101 Firefox/62.0',
    })

    cookie={
        'ASPSESSIONIDASATTRTQ':	'PELLGBGDJJKJOOMCPBAIHKFG',
        'ASPSESSIONIDQADBADCD':	'IDCGNAHDALIGKPCIKCEPKKFH',
        'ASPSESSIONIDSSRTARDD':	'HPAMHOPBLHKHEMGJODLMJGNN',
    }

    payload={
    '__EVENTARGUMENT':'',	
    '__EVENTTARGET':'',	
    '__EVENTVALIDATION':EVENTVALIDATION,
    '__LASTFOCUS':'',	
    '__VIEWSTATE':	viewstate,
    '__VIEWSTATEGENERATOR':	'C3E8EA98',
    'Lotto649Control_history$btnSubmit':	'查詢',
    'Lotto649Control_history$chk':	'radYM',
    'Lotto649Control_history$DropDownList1':	'2',
    'Lotto649Control_history$dropMonth':	month,
    'Lotto649Control_history$dropYear':	year,
    }
    
    req=requests.post(url,headers=headers,cookies=cookie,data=payload)
    return req.text

#分析html
def Extract(text):
    loto_list=list()
    
    df=pd.read_html(text)
    df[0].to_csv('tmp.csv')
    start=4
    with open ('tmp.csv',encoding='utf-8') as f:
        
        content=f.readlines()        
        #取得csv的行數
        max_len=len(content)     
        
        while True:          
           #csv行數小於start離開迴圈 
           if start>max_len:
              break

           #期號-第4行的倍數 
           if content[start] is not None:
              peroidnumber=content[start].split(',')[1]
              end=start+3
           
           #號碼在7的倍數 
           if content[end] is not None:            
              splitstr=content[end].split(',')                   
              lotos=splitstr[2:9]        
              #計算每個號碼出現次數
              GroupData(lotos)            
              #下一行在end+9
              start=end+9

def DrawPie_Max():
    global group_dict
    出現次數=list(group_dict.values())
    np_total=np.array(出現次數) 
    fig = plt.figure("熱門出現次數圓餅圖")
    fig.set_figwidth(300)
    fig.set_figheight(300)
    plt.pie(np_total , labels = loto_range,autopct='%1.1f%%')
    plt.axis('equal')
    plt.show()

#熱門統計
def DrawBar_Max():
   #https://ithelp.ithome.com.tw/articles/10196410    
   global group_dict
   出現次數=list(group_dict.values())
  
   np_total=np.array(出現次數) 
   fig = plt.figure("熱門出現統計圖")
   fig.set_figwidth(300)
   
   barlist=plt.bar(loto_range, np_total)
   plt.xlabel('loto number')
   plt.ylabel('count')
   plt.grid(True)
   plt.show()

#冷門統計1
def DrawBar_Min():
   global group_dict
   
   出現次數=list(group_dict.values())
   maxcount=max(出現次數)
   np_total=np.array(出現次數) 
   np_total= abs(np_total  - maxcount)
   #print(np_total)
   
   fig = plt.figure("冷門出現次數統計圖")
   fig.set_figwidth(300)
   bars=plt.bar(loto_range, np_total)
   for baritem in bars:
       baritem.set_color('r')

   plt.xlabel('loto number')
   plt.ylabel('count')
   plt.grid(True)
   plt.show()


#統計每個數字出現的次數
def GroupData(lotos):
    global group_dict
    print(lotos)
    
    for loto in lotos:
        if group_dict.get(loto) is not None:
           group_dict[loto]=group_dict[loto]+1

if __name__=='__main__':
   
    Initial()

    for month in range(5,11):
        print("抓取第:",month,"個月的資料")
        html=ExcuteCrawler('107',str(month))
        Extract(html)
        time.sleep(3)

    DrawBar_Max()
    #DrawBar_Min()
    #DrawPie_Max()
