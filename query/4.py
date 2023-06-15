from db.db import cursor
import datetime
from datetime import datetime

if __name__ == '__main__':
    ins = """
    with product_name as (select uid, `name` from product)

    select product_uid, `name`, track_number, buy_time, promised_time, actual_time from shipment as p1
    left join product as p2 on p1.product_uid = p2.uid and p1.promised_time != p1.actual_time;
    """
    cursor.execute(ins)
    for data in cursor.fetchall():
        print("product_uid: %s, name: %s, track_number: %d, buy_time: %s, promised_time: %s, actual_time: %s" % (data[0], data[1], data[2], data[3].strftime("%Y-%m-%d %H:%M")
                                                                     , data[4].strftime("%Y-%m-%d %H:%M"), data[5].strftime("%Y-%m-%d %H:%M")))