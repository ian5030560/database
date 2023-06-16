import pymysql as sql

__host = "140.127.74.226"
__user = "411077016"
__password = "411077016"
__db = "411077016"

connect = sql.connect(host = __host, user = __user, password = __password, database = __db)

cursor = connect.cursor()