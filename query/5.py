from db.db import cursor


if __name__ == '__main__':
    ins = """
    select `name`, address, phone from online_customer
    where uid = (select customer_uid from shipment where track_number = '123456')
    """
    cursor.execute(ins)
    customer_info = cursor.fetchall()[0]
    print("Customer Info: name: %s, address: %s, phone: %s" % (customer_info[0], customer_info[1], customer_info[2]))
    
    ins = """
    delete from shipment where track_number = '123456'
    """
    cursor.execute(ins)
    print("Deleted shipment info where track_number = '123456'")
    
    ins = """
    INSERT INTO shipment (track_number, shipper_uid, customer_uid, promised_time, actual_time, product_uid, buy_cost, amount, buy_time)
    VALUES ('123456', '1', '1', '2023-06-16 12:00:00', '2023-06-16 13:00:00', '1', 100, 5, '2023-06-16 11:30:00');

    """
    cursor.execute(ins)
    print("Inserted new shipment data")