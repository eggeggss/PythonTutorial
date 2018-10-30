import numpy as np
import pyqtgraph as pg
import time
import random as rd
import multiprocessing as mp
from pyqtgraph.Qt import QtGui, QtCore
import psutil
time_serial=0
last_time=0
datas=dict()
N=100000

#y軸
datay=mp.Array('f',[0]*N)
datay2=mp.Array('f',[0]*N)

#x軸
datax=mp.Array('f',[0]*N)

def DrawLine():
    nx=np.array(datax)
    nx=nx * 0.01

    curve1.setData(x=nx,y=list(datay))    
    curve2.setData(x=nx,y=list(datay2))
    

def InvokeQt():
    global time_serial,datas,curve1,curve2

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

        curve1=p.plot(pen='r',name='cpu rate')       
        curve2=p.plot(pen='g',name='memory')
        
        timer=pg.QtCore.QTimer()
        timer.timeout.connect(DrawLine)
        #1000是1秒
        timer.start(1000)
        
        QtGui.QApplication.instance().exec_()
        #app.exec_()

    except Exception as e:
        print(e)

def OutputData(datay,datax,datay2):

    time_serial=0
    loop_serial=0
    while True:
        #time.sleep(1)
        time.sleep(0.009)

        if time_serial>=99999:
           time_serial=0
        else:
           time_serial=time_serial+1         
        loop_serial=loop_serial+1

        data=psutil.cpu_percent()
        datay[time_serial]=data
        
        data2=psutil.virtual_memory().available/100000000      
        datay2[time_serial]=data2
         #rd.randint(1,11)

        datax[time_serial]=loop_serial

if __name__=='__main__':
    
    p1=mp.Process(target=OutputData,args=(datay,datax,datay2))
    p1.start()
    InvokeQt()
    p1.join()
    
    