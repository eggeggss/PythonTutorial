import dao
import net

#從資料庫抓取資料
mydb=dao.DAO()
mydb.get()

#從網路抓取資料
net.GetDataFromNetwork()