import requests
import pandas as pd
import time
import matplotlib.pyplot as plt
import numpy as np
import operator
import os
url='http://www.taiwanlottery.com.tw/lotto/superlotto638/history.aspx'

EVENTVALIDATION='urU8i4MnNejdgk2i9kCaQqHnrjZTNFC5PIEdHzl/44FtAjDJHMmM66iCj1Oe6kALr1pAeMyTvGZwQOM+Fmg0o44NoVvqEB74kS8gYuJrPrHC7uOSQVRPHXb1QAMvhAc851tNn5CwLHsX5Ljev+Y8QEf1Zaz1BzldI4fPGIwlkwASB0IjkbHWdfou4pkc/Mx3tthtz/8F2hiP5b0oxLtfudHjFgGixdzRLLi7l7r+/U0ApZiC8w67KmZctftc8RBYzuB/bCIfC2BNWJqZzzG1dTSSUZ5EkRN5rfUM0JJVyBIQjqfUuu2hHgVsz5pDKQlGEisgegfsA20gjSw4Ax9hDq3g18Qp80NfV0TTp5YeHbZHq+nz9AeV5hehLZRGx88HzSkAS+pwkPBg6ql2hoGP07hQdq69IIdGAk/r93nLQrkmm2YCgbDKqnN/Zv/sna+kcN0k+T0mnQFlipda9pGp7665oOSMm3nr33tq7odWvHeD94/GSwyHQXuIYOpxv7YfnQAgVE8Rcx3PEEgWQ9oZA2AdFSQz7BzgF2k8dFlpAU04AZC33wbEb91xDE41s4EhTySTXBdtmCSyIxd41LqU+ScHj3a4/F478XzIC22f2Nl89Y7s/T8y/fxNAJnxwqh7kK90tAhoUGgOq9AkjpPWzVwmaVlYWTUxE7zh3V6cZ/6NawgWF+acIiNRJAxLlLRbcf6VNeflIbCVm4KMo8/Vyb54zrfnvxxlXxbVpBYNzLi3FDztNWOmWnM9ugJAPgkhagMW/LLgoO7HNRK+OqNFwj1ZV+znZTEng6D7cbQsSEzptqKQ+SMl0M+vApCEsVkRTIjI6w=='

viewstate='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'

first_range=['01','02','03','04','05','06','07','08',\
            '09','10','11','12','13','14','15','16',\
            '17','18','19','20','21','22','23',\
            '24','25','26','27','28','29','30','31',\
            '32','33','34','35','36','37',\
            '38']

second_range=['01','02','03','04','05','06','07','08']

def Initial():
    global group_dict,special_dict
    group_dict=dict()
    special_dict=dict()
    for basenumber in first_range:
        group_dict[basenumber]=0
        
    for basenumber in second_range:
        special_dict[basenumber]=0

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
        'Cookie':'ASPSESSIONIDSSRTARDD=HPAMHOPBLHKHEMGJODLMJGNN; ASPSESSIONIDASATTRTQ=PELLGBGDJJKJOOMCPBAIHKFG; ASPSESSIONIDQADBADCD=IDCGNAHDALIGKPCIKCEPKKFH; ASPSESSIONIDASDQRSSR=PLLMCNCAEGHOKBBHPNMKEKEG',
        'Host':	'www.taiwanlottery.com.tw',
        'Pragma':	'no-cache',
        'Referer':	'http://www.taiwanlottery.com.tw/lotto/superlotto638/history.aspx',
        'Upgrade-Insecure-Requests':	'1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:62.0) Gecko/20100101 Firefox/62.0',
    })

    cookie={      	
        'ASPSESSIONIDASATTRTQ':	'PELLGBGDJJKJOOMCPBAIHKFG',
        'ASPSESSIONIDASDQRSSR':	'PLLMCNCAEGHOKBBHPNMKEKEG',
        'ASPSESSIONIDQADBADCD':	'IDCGNAHDALIGKPCIKCEPKKFH',
        'ASPSESSIONIDSSRTARDD':	'HPAMHOPBLHKHEMGJODLMJGNN'
    }

    payload={
        '__EVENTARGUMENT':'',	
        '__EVENTTARGET':'',	
         '__EVENTVALIDATION':EVENTVALIDATION,
        '__LASTFOCUS':'',	
        '__VIEWSTATE':	viewstate,
        '__VIEWSTATEGENERATOR':	'C0CE352E',
        'SuperLotto638Control_history1$btnSubmit':	'查詢',
        'SuperLotto638Control_history1$chk':	'radYM',
        'SuperLotto638Control_history1$DropDownList1':	'1',
        'SuperLotto638Control_history1$dropMonth':	month,
        'SuperLotto638Control_history1$dropYear':	year,

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
              #print(peroidnumber)
              end=start+4
           
           #號碼在7的倍數 
           if content[end] is not None:            
              splitstr=content[end].split(',')                   
              lotos=splitstr[2:8]
              
              #計算每個號碼出現次數
              GeneralGroupData(lotos)  
              SpecialGroupData(splitstr[8])       
              #下一行在end+9
              start=end+9

    os.system('rm tmp.csv')
    


def DrawPie_Max():
    global group_dict
    出現次數=list(group_dict.values())
    np_total=np.array(出現次數) 
    fig = plt.figure("熱門出現次數圓餅圖")
    fig.set_figwidth(300)
    fig.set_figheight(300)
    plt.pie(np_total , labels = first_range,autopct='%1.1f%%')
    #plt.axis('equal')
    plt.show()

#熱門統計
def DrawBar_Max():
   #https://ithelp.ithome.com.tw/articles/10196410    
   global group_dict,special_dict
   
   #根據values降冪排序
   group_dict = dict(sorted(group_dict.items(), key=operator.itemgetter(1),reverse=True))
   
   loto_range=list(group_dict.keys())
   
   出現次數=list(group_dict.values())
   np_total=np.array(出現次數)

   fig = plt.figure("熱門出現統計圖")
   fig.set_figwidth(300)
   
   #前6筆highlight
   barlist=plt.bar(loto_range, np_total,color='b')

   for item in barlist[:6]:
       item.set_color('r')
   
   plt.bar(list(special_dict.keys()),np.array(list(special_dict.values())),color='g')

   plt.legend(['First Section', 'Second Section'], loc='upper center')
   plt.xlabel('power number')
   plt.ylabel('count')
   plt.grid(True)
   plt.show()



#統計每個數字出現的次數
def GeneralGroupData(lotos):
    global group_dict  
    for loto in lotos:
        if group_dict.get(loto) is not None:
           group_dict[loto]=group_dict[loto]+1

#統計特別號出現的次數
def SpecialGroupData(loto):
    global special_dict
    if special_dict.get(loto) is not None:
       special_dict[loto]=special_dict[loto]+1

if __name__=='__main__':
    

    Initial()
    #1~10
    for month in range(5,11):
        print("抓取第:",month,"個月的資料")
        html=ExcuteCrawler('107',str(month))
        Extract(html)
        time.sleep(3)

    DrawBar_Max()
    #DrawPie_Max()
