from manufacture import dbForMfg as dbm,methodForMfg as methodm
from finance import dbForFin as dbf,methodForFin as methodf
from distribution import dbForDis,methodForDis

#使用製造模組的方法
mfgdb=dbm.MfgDB()
mfgdb.get()
methodm.printMethodName()

print('*********此為分隔線***********')

#使用財務模組的方法
findb=dbf.FinDB()
findb.get()
methodf.printMethodName()

