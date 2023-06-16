import pymysql as sql
__host = "140.127.74.226"
__user = "411077016"
__password = "411077016"
__db = "411077016"

__connect = sql.connect(host = __host, user = __user, password = __password, database = __db)

cursor = __connect.cursor()

def getStoreInfo(region):
    cursor.execute("select * from store where region = '%s'" % region)
    return cursor.fetchall()
def getStoreStock(store_uid):
    cursor.execute("select product_uid, `name`, current_amount from inventory as I join product as P on I.product_uid = P.uid and I.store_uid = '%s'" % store_uid)
    return cursor.fetchall()
def findStoreUid(storeName):
    cursor.execute("select uid from store where name = '%s'" % storeName)
    return cursor.fetchone()