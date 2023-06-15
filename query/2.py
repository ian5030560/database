from db.db import cursor


if __name__ == '__main__':
    ins = """
    SELECT uid, name, sale_amount FROM product
    GROUP BY uid
    ORDER BY sale_amount DESC
    LIMIT 2;
    """
    cursor.execute(ins)
    
    for row in cursor.fetchall():
        print("uid: %s, name: %s, sale_amount: %s"%(row[0], row[1], row[2]))
