import numpy as np
import pyqtgraph as pg
import time
import random as rd
import multiprocessing as mp
from pyqtgraph.Qt import QtGui, QtCore
time_serial=0
last_time=0
datas=dict()
N=5000
datay=mp.Array('i',[0]*N)
datax=mp.Array('i',[0]*N)

def plotData():
    nx=np.array(datax)
    nx=nx * 0.0001

    curve1.setData(x=nx,y=list(datay))
    

def InvokeQt():
    global time_serial,datas,curve1

    try:
        #app=pg.mkQApp()
        app = QtGui.QApplication([])

        win=pg.GraphicsWindow()
        win.setWindowTitle('demo')
        win.resize(800,400)

        p=win.addPlot()
        p.showGrid(x=True, y=True)
        p.setLabel(axis='left', text='x')
        p.setLabel(axis='bottom', text='y')
        p.setTitle('demo graph')
        p.addLegend()

        curve1=p.plot(pen='r',name='y1')
        
        timer=pg.QtCore.QTimer()
        timer.timeout.connect(plotData)
        #1000是1秒
        timer.start(500)
        
        QtGui.QApplication.instance().exec_()
        #app.exec_()

    except Exception as e:
        print(e)

def OutputData(datay,datax):

    time_serial=0
    loop_serial=0
    while True:
        time.sleep(0.001)
        if time_serial>=4999:
           time_serial=0
        else:
           time_serial=time_serial+1         
        loop_serial=loop_serial+1

        #
        datay[time_serial]=rd.randint(1,1001)
        
        datax[time_serial]=loop_serial

if __name__=='__main__':
    
    p1=mp.Process(target=OutputData,args=(datay,datax,))

    p1.start()
    InvokeQt()
    p1.join()
    
    