import requests
import pandas as pd
import time
import matplotlib.pyplot as plt
import numpy as np
import operator
url='http://www.taiwanlottery.com.tw/Lotto/Lotto649/history.aspx'


EVENTVALIDATION='YASQNAiVmEXzYiHWSht+vDSrRa3i0/TPFcZh21AoOlKKkrZOH4ukS9S8JlFDGi1N2E3QNLOZ0wuxe4QnfvebzWzng481dzGK1yi1Wm7wOjLtuF92iAhhbr0/eBbL43/cCh0md0bwzdkdW5qLSvL57o/k3HI2fyaufP7IYat9UCkTP43C01OGnNP8s8KelddPAVpblvrveTnwwOiwitXETFt0sZLO3m2wTFB0pcO+P3ijzR0BAtGBBNHzWDj6caLbwbvvFzO4Nu1kL5abLBLzbOY2/DwmVmdYZxvw5zvK0omRZDXmDs1LikatxzKb52/tAJ8w6oAguGxfhJz/l8l4E5W24UPW+ZaEHJuEPp6m+KehMovRrHlw89q7m+IKr0hv+91DZyyJ/ppwzNsexKmp1DsXb/Imgz6F4airOLOJSfcUYEmU9JWNgm3MjxsqoxuNKOkjW5yvSUYdoTkf8MwFqglEz2PyrxMQpMPwGzJsqr6ptADnAPgq/z42an+TDp/U+MlxfWaWT2/iFWw/qqbLgLPCkyULtp0SxvY5kVIQsth1X9Q+YQDMSKthnFIrhRme7XvNgSNJCbEeULOkDrKyTYzbwMIlsBgs72OJDou60qv4Y6jKkgGCoC5Y9sPJ5XQqzaljXteueHjUn8BzPhwjmxW4iL4ILfG0AZow4btRF/6kVXU6RbghmCKHPqPdGgo3yLiV5pll3p2A5wpjvn95vuHw9M09vXYmjgaFQfDhUQM1UBqXywNj31d+zw7try5sdpeIkZED3quexeNgCDUERhiAPpxGcWw5vvVDExBxEE8O7vqzU81I8ryWHGb0uX/eWTxxfg=='

viewstate='BfY+nEE9M1y6DKaC8ucxXDatUxNhE88qSxScmkpoFnZy+LEM3C6uZ91ZHQy1mxOLhErv2YSWthPmt/IwY1R4HZlefjyF98OprWnkYsAmc7vauBdwEic8YsT+InXXLpJ1t5Gpl66VBJCv60m3VEw5dNntQ+9X5F1PE3OfOH1ISnQGUa0/E4PbIrHNOrNhVvhQe9Z4MJkcOBOy+NHzJVnad8CrvfF/ORK3tfLzeAXMh57CUf2tv35UCuICkdzTcoKvWOAWfs7SbGZpqqPVHX3CVdNsVS4Xcahn+NSzf97WVGnKyIFmjml/W2ty/iIRUHJ9KlcFc6EAJo9K3O3wJaHwULT13okd5dt5XEnlR+Qv8UzaaAXVuaGi2wrBcluxMWoDCqkLElNtsHOKjk51Cpi36RSFWsMSL3p0MsKIbEhkPPumqIJ5fl6kMS/kmv4nyECrgZzmCiKJU4Ly+F2cXATU8l7FuczJTUmYEPhV3uqI2hwAM+N3EyR65IE4bDyWy/qqTqUOxaQdnvfo5xaEKSH9tLj/uYl1nfGSFNqPqha1CYqMuQZYSLRs1giQNznMBdK8OBu6PaAVfpMi1baFRG61LbSl5KZOBzVmP6n2Dk4PgmDMEqkflH6UJnv7u6Pth9A2Oe/uW2N7PfPNd1Y7y5RsQ+ub8ldGfd27Vj1JkF5SYIkvFux0h/byCPNC1SSHNpdyy4Uo3BVtX+jGmd6taOtnIECsFeC4jXHPmO2X5lUH6/trwkgncPJ5bL+lWKMXUk27reGqiRdfe6NT8FLwrb9EMLXPoylOIY5e8TnCiSh0T5PyNj98DKZ0E6XfOD6qy367ezXB+klyBygjp95e+9a8w7JANhxEyxSVZfruidZizxxv6ySwe/XAYffmvPDx+UJrM3hnZQsgsPOq4p0nvw+ncQewLSWNvF1ej0noSjMOHFtD0GNvX9K8H7azsuiFlkQ4mWwmpFU1tEblavdaqsE/UjZ/itPzj9sNwlf8sqJCCRfELf85HNZ1wI8Gx8k1PwK9Zn1zJPbtaZpuO6pCO+g9jAer5JMReitZG69F9Q/YtilTXHuFr2pJA/n08CgsX4n+/ky4tz3vZdkLF/4cYxI/NQCa7BV/F1tteQjivUQcFgW58b3Ti/i/bSnej6Y592a8JZ4SBdaDxj8naBx97rQ4kzRYb0hDPrYbkLZGXhGlBZa6yVjaIU9Mumx9662dmYY7iDQkGZ0JyuNsvxEyyZeavuk7YPU13bKMEaBMbAotB8LAtjbbFS5BlEr8VB3GMBPNDmPk8G3ZY/siJ2Fx0LohgoHvmFHhWiRVHqpXNYmWr6edep+oSCMUtmIKQlm3LNJRETSVWu/euD2ht9KxClGKWqggspR/vyKT3+yUiDmyHvjKt562GBUWQkndZO6/Ry+/oYfQhTeqE0+Z+pT2CeI2J8NJslpliU52P/WfHEP0BLP50b3rRWaBfj/daO5N0cRcfsb6/IfIsOB7b710mpSFoA3Ju3kycUlUsUOxhc1bxXzto2rcwsmsOk8HlSZ0jJl0kAY5twb420bjZtAPLqbF6nph7iZ5fN9AxF2PtwoSazTX0SKkJVR7iDxxXsmDvOal4un6hRMFAyS+EJjTA6EMGnr2bhwrTApInSmeAiR2xv7TPHo5AHLydcAbyrb1HZSTdQ/K4GsQvhHpwuzSWMGeMfC4oMBWAwsITxOA/r/xwrPu0p+OQPOn34CGfOqFp1tmGR38ol0AHppp35QO+R3pnQEMkVs1zPXGfheTpNgLeFUcBEPV7g4NA8Dr/HNIeyB0ZXL5M1/3gxADHLbQwpOBceFEE0MglxT4vXsTZB9UI/8WXZDhO+xP26NGJ56Zeaxq81z3EiFDnx1WOtNaPJp6OWSLEzGwPxnXBwFWDKnn75fFgCXhvHTgFMwZfpa3urCAHhQBQN8VyIJia90jmucBIRH7OuR9t8D7bMdmyb7hKO9oB+mR8XRjPSPEDWGW/mzPRHSTMpVq3QZ+MNc7gtXvg7dDe9hD73ADHOqmn9p+M1ww71cIz14g5D7s922GgHoTpXNcT2hQY8KVahVp5O77MTllD37KZt75Yc6FUrJF4VimhpD8Zu3ApRl7FGgbnCQywGdZiUXoau/IbmlTGx6zI9BSaNkREKo5Z+42+a46MTEQ2+SnyKIpeHS7qqzoUFPnkYwpwvH3itbjWEDUZVQ8mOwPyFoXk93kP1Nsz1FhHgI6oUBz2q46LdaSaSUKxcQz/unSJBmUG3nxmh2SKFbW0rkiktbNVWmpD9tw5wlW4QbrXBql53M1gA/jeriMvVjcMxmn6PEiIWqbu0kAtBKtHnLGAMNEs+I3XhK1aD0ze7MSjx26t5Kf06BhCraIefSnLnYonvfNZ4s4qGi1USb9vbduY3UlVIHu4oGbjM2KeHiYPNxp0ZP64600FtmCkWqwaD+g0o6V0snjYnEdDqxzQPzbkGF/0MHLpAh0zn85vsgLwu/YARt772EXCrSepywEjKrBSUZwqhiIUmAp1zW6g0A5sS+fyNYPoEWuhav44f0BK9nwJzUm8CX1tVaYOpW6/DDrgNCUVy6ENrqJF4mzTZ/IOIRxGw3DY4J5d15XtnMFyA5jlW5AWtENDbaIp1ZfV5jez/oQ2P6Jm8m8CmB2VCPXOGeJ1UIbFBUiavdXcoG3gT/+vj1E+5vyDAdmz8EoY2mdEqGLjYH6SswO3Q3rrHwm+PXA96iBbUOy44XEZVKHLUspmjI2qV3OyBYBWUQpcuvO2ccaobHcRDz6cS5yfta+NBjKETitXaaicjxFaz2QfQe9UJN/Slc2pfBYy1xKcd3x2h4Sb9/74XVWFiPxb14JJGKJXnVrYRS94j1IZWUUwuyIDBoPm9UhGavkDgMohii92AkMhxtDfyBv4hMkBYxqRJ/bIurvWnb0RhucAggMPhV5RFtKP5zHcyTJ0ckX06+NX53e8AdKPFmgTjM+yggtQrmEek3L3j5mFjjTXXfJG7zvXtKhAPXB7s8OCoAu/fj9FXV8anM6og0fiHaNZw6wW5HoT1TajhDQlDeXmDvhcS5Ta82HkpqNLafgbL0Yc8hiuSZp6p3zlRhy3mvtQdIozbdC+9wyBpmb+lVgrpqDg/l5VMwwcUfrxhvOIAE9gXbtmNXsRaU0O+VbU7hog/2/VqPSvCACfdqXAQIjg/cNCagAf1vIb8FGVHoVFnNsz2Hp6/aZY3i4zGNDxQV91MwJMG7vnFHGFnnk61aQczp+ukS5DcvOwLsKGYVZDin5HodqdpTRXyYALaTqC3vAHZaDHdyFlhFEIVYH1PfrWjrd5KX0ShixSXzOMdpGzVGcR4a7bYZibKSmW3qvgqxxkLJiATF53iiFo4MTtGMJRAxlszujcOdFVMIatNiLTSTJHpPA8lFlfBQJ5kkQ8sDlT1856qjC7Jc8SprknAJGMhrO25pz7lVl09dI+MaCF2VHGSQdOlznlBke/xJlXelzOhYuqkFOUSyGPxv0QpqamvkZuWf7Ah73v/aBvk6h3+oKo8mLV8s/fwY5p//JBkZwNv+zu65kF0Rbb2yUNt8dadL3s7rT9hOAUk/kCP3mT3+PbMiYfRlnBmzVbJgkd94XeY13CIRp2IsUgWj1faD+3ZfiVRuv8eCp7LUBaZO5TRm16i+NcVgEuWBw0MsUMm29aBZ574uPcXW7Jugqdee8W/XM5P+dv19NJIDGAh0A1VfC1u8+Sqoad1Ycc95HxUOrDFlr1AJL0YqlDPyvEfSzwu3RYrAzy3meZwNcOPbBYQc1vM81wXwzJs9zzM9BEV3oVCsx//euOSpZ+Cjl89JAFnq+c1zMuZPYGVUf7r3Urc5WN8TJ6eMlze5hfR5Q/6VsR2uXnXcDbnOBK8AgxiCn0s9lZaUn94tnZs8krUnANmS6PabY3tNEghGC9WannwhudLFXQW+xGnLH1uM+B1p2y9Cdd7RfACxNQiMGWWzrdoS2Or/2Cq5FIae6BLcGinQk1n+1eYa/+hSYBWY4yZmDanpf9OkE9qhtH4kODUgRlCv+mCjvvtFlT7+Bg4NWoE4Wf0gCHLu/HPRn3VWgeB4+6RK+LF85kpBulZhX9j4iznwf6/wK6d/DteRxNKGvknjKGLwyPyIUccvbO7FWLAnJebNFMchz/4ZVEeObXLkcRsoiI+3woWpF6/e/ooQ6nnqj4nJbab5TSSdjTcQMlx2ebQJoi6cKCCEyYfL4yS5ky9v2x7l3Nhiu54yvPRTnH6qzCuAdKW3CO+kDiB13X2MxrE2zuNjWbU2XEGvK2oSTwuJr/m15a+pwkSsCzpsU/cDxXassEtcqb4KFG7GlFP69eK1OyBWvPC+EPUzWOvUxMhsgkFepaCYTgexvb2UlqLjndwJM7L0ZZmiC3PFs1syej710ViE1tLP54u5mH/t7sSs4SQfJGI15ap5QreN0pZOTNW2o9pPs5WK4hqqk/eIr7eU/Rmd/aSwWfDvhYas58wIxwRJy+VOVI8WgIA0huCiArbgm5rabq7UnU4jHYdrIYjj0Or/APo0+jtz+lJ1obNTeYKne2yYVCGP/yn+GObuNDDo4JnCX8qJBzgV/HQL8qNK0gpIRLEzNEpGWqv5aiJqy/qgQMATwpX/dCfp6/sXoRYJxmVYitCOcYVIN7hWsy7xQMcrzSNTiGF5/Z2sIawHuc0ZI+yTZimET09Q3JA6CRGP4cn/zPruNtuiITpYhEDObjVLj1Cd+SIRmg/3ZSa1LNiNGNHIO+FrE6iy5qpJFkm+XoPyaBSl/ISul14TYyuM8raaHE2XCqsXMaCFfGzvrBFQ3lR3NxL1FcnJrPvXjqS798Zdmhrw38yAxY8EAbnvwyNyI9hJpHp+bnHhsmaUubS9NusRxtPeunPECz2GvRiR98/YM13I/1N4yDTX3ZQhhops4hBTZbnNYe+pT2YRgCmuC3ct54l/sTfggwaqy7/XTisclCv7aouk7flCGm5fnPV/A1MwHiSc3vzzXSWz2wOVpoAblBm67N3FToGUl69nJLhi4yaZq5+lGxie/71/wjHlLs8TmBCUstU5QQP2ejVWmVCakPtwAN5ZWn4DVaZN6w+/5YK/J4+/06sldNZm8Kv2KzDfz45FhZtFYCIlSxtBLuPyws1y4NWlKDqS4Pqi7JEHtWK/T1OsNMicVj7g/7aEMsMIklfgDRGAmfAG0NgMypEO8AopmohFvm8SY3K3Bey6jCKCAzqfCQopebdCDCdiPzyCUZTiOY63SYPfIgL1d4mL0f6Hm75DTyOhK4F3WB8RD+vuDypJkG0lxp2VRK4wKPcjHuva812XFtArsMF3wCUNEp7QRUaDCMB0dl4DA7fYKUOZImOXq7s98cqGb96XfP7YeUgSfY9Do+uQeAMRTN2daYS7f7/hR7a3c4fk35k+xgJF07hR13MYJl/UoDqzZPcHUqWUrugAJura6t+/RDpaERxcTGIqAzwAkGXshTvP/D90xUjoqQbsPCf8oXavhrhq813kgBLFPV7aYDodGR6NchwAYRXTYwaLWqRex8HVZWKsfa1e0XI0vYV8QX3QdZW/hmL+nHhrhmCGEhoXkyNb9qBhNASoGUOiLKJc1DzwEy+BSPMKtLMkn7wEydOAzZLBhORTiKjP0PESdCbDifpnzaq5+DL27ShSroCLYUlmdx9ZXvKw3gwTm2BcBwEQp4auPsCi7whKRrJePZspbTbgZFqPIaQTve05x+U5FAgKKj7BybiildhPriaQPjazY23qR0tPvkFcY9YOIoTEqOyVidOQtwAg+6R9q7HMTi3lWoXDWMGmwl1pgk+jT5BZSiEox2aFejIiW0mlJ/g8gzAVVXUNeIMRibVmAevdlcv574I4nr3KSejuqDj2vxlNtJBxAWhHhL6Sbth5Z9QNXswf8Q7ZytOSkpizX0BCyqXkuzSecPnwcPt7unCrsk/Ut3ymv/iP6/OYfyjIRjMQXNKR+4fZEPVmMGAKGzbr6ceH6hdY+7nQQjtdTnBLciA66ZNQDvjhRt/i136I+P3zEfaMruxi4SlCXrlkRNgvFjaPEb6YaIDh51smT3/e7KD0HS7h/XljPWai4hEz0HxKYpPJgBTdJahb+1VTYKKdREhSdAdBDv4R7+ZMb0vLbwiX/sMJXD3csnLHqi3GqL5UGlwipsVneU04ZItz0lvjIcjbt3z2y1AI+qS6yW5DLLBIO+gH97xoM6eddZnA0mx5GYXbSULRRJhPWFBCM1Fl+lfOskkpspH/u7//Vu/J5rU0zJX7PqGOXpGX5TFjxlNJPX7iLInpy8v0G7l9AL/mXEvv38kQOB8i4N+A7Ct1NoxAQaXBLiVLBewJeAtOqSoH//VlwJz6ZTnaIZsyemU9XnJyIl6QZNZ5pTEVmHRSVm2NK'


loto_range=['01','02','03','04','05','06','07','08',\
            '09','10','11','12','13','14','15','16',\
            '17','18','19','20','21','22','23',\
            '24','25','26','27','28','29','30','31',\
            '32','33','34','35','36','37',\
            '38','39','40','41','42','43',\
            '44','45','46','47','48','49']

def Initial():
    global group_dict,special_dict
    group_dict=dict()
    special_dict=dict()
    for basenumber in loto_range:
        group_dict[basenumber]=0
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

   plt.legend(['General', 'Special'], loc='upper right')
   plt.xlabel('loto number')
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
