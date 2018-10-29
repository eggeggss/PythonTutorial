import numpy as np
import pyqtgraph as pg
import time
import random as rd
app=pg.mkQApp()

win=pg.GraphicsWindow()
win.setWindowTitle('demo')
win.resize(800,400)

p=win.addPlot()
p.showGrid(x=True, y=True)
p.setLabel(axis='left', text='x')
p.setLabel(axis='bottom', text='y')
p.setTitle('demo graph')
p.addLegend()

#test123
curve1=p.plot(pen='r',name='y1')
time_serial=0
last_time=0
datas=dict()
def plotData():
    
    global time_serial,datas,last_time
    time_serial=time_serial+1000  
    
    if len(datas)>1000:
        firstkey=next(iter(datas))
        datas.pop(firstkey)  
        x=np.array(list(datas.keys()))
        x/1000
        y=list(datas.values())
        curve1.setData(x=x,y=y)
               
    datas[time_serial]=rd.randint(1,1001)
    
     
timer=pg.QtCore.QTimer()
timer.timeout.connect(plotData)
#1000是1秒
timer.start(1)

app.exec_()
