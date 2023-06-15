from db.db import cursor


if __name__ == '__main__':
    ins = """
    SELECT product.uid, product.`name` FROM inventory AS i
    JOIN product ON product.uid = i.product_uid 
    JOIN store ON store.uid = i.store_uid 
    WHERE region = 'Kaohsiung' 
    AND arrived IN (SELECT MAX(arrived) FROM inventory WHERE product_uid = i.product_uid) 
    AND current_amount = 0;
    """
    cursor.execute(ins)
    
    for row in cursor.fetchall():
        print("uid: %s, name: %s"%(row[0], row[1]))