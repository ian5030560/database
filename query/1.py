from db.db import cursor


if __name__ == '__main__':
    ins = """
    SELECT uid, `name` FROM record 
    JOIN online_customer ON online_customer.uid = record.customer_uid 
    WHERE buy_time BETWEEN DATE(CURDATE() - INTERVAL 1 YEAR) AND CURDATE()
    GROUP BY customer_uid 
    ORDER BY SUM(cost) 
    DESC LIMIT 1;
    """
    cursor.execute(ins)

    data = cursor.fetchone()
    print("uid: %s name: %s"%(data[0], data[1]))