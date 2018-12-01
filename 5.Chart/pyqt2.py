import numpy as np
import pyqtgraph as pg
import time
import random as rd
import multiprocessing as mp
from multiprocessing import Queue
from pyqtgraph.Qt import QtGui, QtCore
import psutil

index=0
last_time=0
datas=dict()
N=100000

#y軸
datay=mp.Array('f',[0]*N)
datay2=mp.Array('f',[0]*N)
datay3=mp.Array('f',[0]*N)
#x軸
datax=mp.Array('f',[0]*N)
queue_list=list()

def GetArdunioData():

    xg=rd.randint(40,51)
    yg=psutil.cpu_percent()
    zg=psutil.virtual_memory().available/100000000 
   
    return (xg,yg,zg)

#畫線
def DrawLine():
    global queue_list
    nx=np.array(datax)
    nx=nx * 0.01
    
    #print (queue.get())
    #curve2.setData(x=nx,y=queue_list)
    curve1.setData(x=nx,y=list(datay))    
    curve2.setData(x=nx,y=list(datay2))
    curve3.setData(x=nx,y=list(datay3))
    
#初始化pyqt套件
def InvokeQt():
    global index,datas,curve1,curve2,curve3

    try:
        #app=pg.mkQApp()
        app = QtGui.QApplication([])

        win=pg.GraphicsWindow()
        win.setWindowTitle('demo')
        #win.resize(800,400)
        win.setGeometry(100,10, 1200,400 ) 

        p=win.addPlot()
        p.setRange(yRange=[0,100])
        
        p.showGrid(x=True, y=True)
        p.setLabel(axis='left', text='x')
        p.setLabel(axis='bottom', text='y')
        p.setTitle('demo graph')
        p.addLegend()

        curve1=p.plot(pen='#FFA54F',name='cpu rate')       
        curve2=p.plot(pen='g',name='memory')
        curve3=p.plot(pen='b',name='Internet')
        
        timer=pg.QtCore.QTimer()
        timer.timeout.connect(DrawLine)
        #1000是1秒
        timer.start(1000)
        
        QtGui.QApplication.instance().exec_()
        #app.exec_()

    except Exception as e:
        print(e)


#把ardunio的資料讀到陣列中
#另一個process在做的事
def OutputData(datay,datax,datay2,datay3,l):

    index=0
    loop_serial=0
    while True:
        #time.sleep(1)
        #time.sleep(0.009)
        time.sleep(0.1)

        if index>=99999:
           index=0
        else:
           index=index+1  

        loop_serial=loop_serial+1
        l.acquire() 
        datas=GetArdunioData()
        l.release()

        datay3[index]=datas[0]
        datay[index]=datas[1]
        datay2[index]=datas[2]
        
        datax[index]=loop_serial
        
    
        

if __name__=='__main__':
    
    l=mp.Lock()
    p1=mp.Process(target=OutputData,args=(datay,datax,datay2,datay3,l,))
    p1.start()
    InvokeQt()
    #p1.join()
    
    #print(psutil.net_io_counters(pernic=True, nowrap=True))
    #print(psutil.net_io_counters(pernic=False, nowrap=True).bytes_recv/10000000)
    