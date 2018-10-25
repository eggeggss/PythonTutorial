import requests
import pandas as pd
import time
import matplotlib.pyplot as plt
import numpy as np
import operator
url='http://www.taiwanlottery.com.tw/lotto/superlotto638/history.aspx'

EVENTVALIDATION='vJqePwdOqHzhsgkg1nXQ9HN3jTFSxuHcoTiq+g+WoXBDxKHeNRvyfc5oucC8fVrvFN8cJcZcg66EoIdkOR7Rv84m3NseshQdgrJL/8ujnAtEJOy5159fAMV9RUEhlovQjtT5HrX4QEXCLTgMf57cvwZWSSKTGAncjkYCC1TXi8vtsrRsun7Szb/1nxBru/41RGWeSMCrKJ4bJQrTFFiiOA2YgpuYPRFDG7E7rtX7KFiQL75un2t2iTnHY2FRQZb8PcdRrQzvLaaY9F0UIUmvIW1vc9cYoyCmV5kpnW6kaWhFM2AGdTotbS7e0txeajqx/PsisaIZO4vwsyDidRhvE0/UyAq+6IrIbFgoOSFpSsLB/dc5yuTtnsNS96uzcJ4Z7lzqSJavKjd49m8BScVZzq6D8ONGl9KEkg/rxtwf/+lOE6do+tkD7lI9mHFujPK4n3eFjUkYiUK3CpfC3jOnAZaRxl/IzjgehBMJm1WTvLJgicHe2ZOJWGgt8zIVhGRyEzoL/yModEwT4A0NxPtC4peafW7yaop32Luc8xILxMlETgnhoSqdf8qOS3hLMMnrtpjVdgUHy2eQJbvE/Z3EpNpWo5KfFOQ+SrjdjX1Hib2PCdHAi15Z3q0mye/9QrwkAdUe27an5wOWIrk84Xvs9EpArWHDTBFrWrkUavlSzzUEOZ49Wo/bycBqykZSLy/S9FKi0TDY4Yb8WE3/LMwommyoi7CwawB6JzifkIViy1G7t+ZtfNxkZyKHvq6SRnS2Vxk/ZetrWkqh6zIyDGbHgoR8upXdyhbICPlSLiZSlbLeqmQslIPVMUx9iFARsmZGg+R0jA=='

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
    for month in range(10,11):
        print("抓取第:",month,"個月的資料")
        html=ExcuteCrawler('107',str(month))
        Extract(html)
        time.sleep(3)

    DrawBar_Max()
    
