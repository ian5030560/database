from db.db import cursor, connect
import typing

def db_search(condition: list) -> list:
    ins = "SELECT * FROM inventory WHERE "
    for key in condition:
        value = condition[key]
        if value and not value.isspace():
            if value.isnumeric():
                ins += "`{}` = {} AND ".format(key, value)
            else:
                ins += "`{}` = '{}' AND ".format(key, value)
    
    if ins.find("AND") != -1:
        ins = ins[: len(ins) - 5]
    cursor.execute(ins)
    
    return cursor.fetchall()


def db_update(old: typing.Sequence, new: typing.Sequence):
    ins = """
        UPDATE `inventory
        SET warehouse_uid = '{}', store_uid = '{}', product_uid = '{}',
        shipper_uid = '{}', current_amount = {}, update_amount = {}, 
        cost = {}, arrived = '{}', set_off = '{}'
        WHERE warehouse_uid = '{}' AND store_uid = '{}' AND product_uid = '{}' AND
        shipper_uid = '{}' AND current_amount = {} AND update_amount = {}
        AND cost = {} AND arrived = '{}' AND set_off = '{}';
    """.format(new[0], new[1], new[2], new[3], new[4], new[5], new[6], new[7], new[8],
               old[0], old[1], old[2], old[3], old[4], old[5], old[6], old[7], old[8])
    cursor.execute(ins)
    connect.commit()

def db_delete(data: typing.Sequence):
    ins = """
    DELETE FROM `inventory` WHERE 
    warehouse_uid = '{}' AND store_uid = '{}' AND product_uid = '{}' AND
    shipper_uid = '{}' AND current_amount = {} AND update_amount = {}
    AND cost = {} AND arrived = '{}' AND set_off = '{}';
    """.format(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8])

    cursor.execute(ins)
    connect.commit()