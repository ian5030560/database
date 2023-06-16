CREATE TABLE product(
    uid VARCHAR(20) NOT NULL PRIMARY KEY,
    `name` VARCHAR(20) NOT NULL,
    price INT NOT NULL,
    sale_amount INT NOT NULL
);
CREATE TABLE manufacturer(
    uid VARCHAR(20) NOT NULL PRIMARY KEY,
    `name` VARCHAR(20) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    address VARCHAR(20) NOT NULL
);

CREATE TABLE package(
    uid VARCHAR(20) NOT NULL PRIMARY KEY,
    `name` VARCHAR(20) NOT NULL,
    price INT NOT NULL,
    sale_amount INT NOT NULL
);

CREATE TABLE online_customer(
    uid VARCHAR(20) NOT NULL PRIMARY KEY,
    `name` VARCHAR(20) NOT NULL,
    address VARCHAR(20) NOT NULL,
    phone VARCHAR(20) NOT NULL
);

CREATE TABLE contract(
    uid VARCHAR(20) NOT NULL PRIMARY KEY,
    payment INT NOT NULL,
    monthly_date DATE NOT NULL,
    deadline DATE NOT NULL
);
CREATE TABLE frequent(
    uid VARCHAR(20) NOT NULL PRIMARY KEY,
    `name` VARCHAR(20) NOT NULL,
    address VARCHAR(20) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    contract_uid VARCHAR(20) NOT NULL,
    FOREIGN KEY(uid) REFERENCES online_customer(uid),
    FOREIGN KEY(contract_uid) REFERENCES contract(uid)
);
CREATE TABLE infrequent(
    uid VARCHAR(20) NOT NULL PRIMARY KEY,
    `name` VARCHAR(20) NOT NULL,
    address VARCHAR(20) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    FOREIGN KEY(uid) REFERENCES online_customer(uid)
);
CREATE TABLE card(
    customer_uid VARCHAR(20) NOT NULL,
    card_num VARCHAR(20) NOT NULL PRIMARY KEY,
    FOREIGN KEY(customer_uid) REFERENCES infrequent(uid)
);
CREATE TABLE warehouse(
    uid VARCHAR(20) NOT NULL PRIMARY KEY,
    `name` VARCHAR(20) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    address VARCHAR(20) NOT NULL,
    region VARCHAR(20) NOT NULL
);
CREATE TABLE store(
    uid VARCHAR(20) NOT NULL PRIMARY KEY,
    `name` VARCHAR(20) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    address VARCHAR(20) NOT NULL,
    region VARCHAR(20) NOT NULL
);

CREATE TABLE shipper(
    uid VARCHAR(20) NOT NULL PRIMARY KEY,
    `name` VARCHAR(20) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    address VARCHAR(20) NOT NULL
);
CREATE TABLE shipment(
    track_number INT NOT NULL PRIMARY KEY,
    shipper_uid VARCHAR(20) NOT NULL,
    customer_uid VARCHAR(20) NOT NULL,
    promised_time DATETIME NOT NULL,
    actual_time DATETIME NOT NULL,
    product_uid VARCHAR(20) NOT NULL,
    buy_cost INT NOT NULL,
    amount INT NOT NULL,
    buy_time DATETIME NOT NULL,
    FOREIGN KEY(shipper_uid) REFERENCES shipper(uid),
    FOREIGN KEY(customer_uid) REFERENCES online_customer(uid),
    FOREIGN KEY(product_uid) REFERENCES product(uid)
);
CREATE TABLE inventory(
    warehouse_uid VARCHAR(20) NOT NULL,
    store_uid VARCHAR(20) NOT NULL,
    product_uid VARCHAR(20) NOT NULL,
    shipper_uid VARCHAR(20) NOT NULL,
    current_amount INT NOT NULL,
    update_amount INT NOT NULL,
    cost INT NOT NULL,
    arrived DATETIME NOT NULL,
    set_off DATETIME NOT NULL,
    PRIMARY KEY(
        product_uid,
        store_uid,
        warehouse_uid,
        shipper_uid
    ),
    FOREIGN KEY(product_uid) REFERENCES product(uid),
    FOREIGN KEY(store_uid) REFERENCES store(uid),
    FOREIGN KEY(warehouse_uid) REFERENCES warehouse(uid),
    FOREIGN KEY(shipper_uid) REFERENCES shipper(uid)
);
CREATE TABLE `grouping`(
    `name` VARCHAR(20) NOT NULL,
    product_uid VARCHAR(20) NOT NULL,
    manufacturer_uid VARCHAR(20) NOT NULL,
    package_uid VARCHAR(20),
    FOREIGN KEY(product_uid) REFERENCES product(uid),
    FOREIGN KEY(manufacturer_uid) REFERENCES manufacturer(uid),
    FOREIGN KEY(package_uid) REFERENCES package(uid),
    PRIMARY KEY(product_uid, manufacturer_uid, package_uid)
);

CREATE TABLE sales(
    package_id VARCHAR(20),
    product_uid VARCHAR(20) NOT NULL,
    manufacturer_uid VARCHAR(20) NOT NULL,
    period VARCHAR(20) NOT NULL,
    season VARCHAR(20) NOT NULL,
    store_uid VARCHAR(20) NOT NULL,
    store_region VARCHAR(20) NOT NULL,
    FOREIGN KEY(store_uid) REFERENCES store(uid),
    FOREIGN KEY(package_id) REFERENCES package(uid),
    FOREIGN KEY(manufacturer_uid) REFERENCES manufacturer(uid),
    PRIMARY KEY(product_uid, package_id, manufacturer_uid, store_uid)
);

CREATE TABLE record(
    customer_uid VARCHAR(20) NOT NULL,
    product_uid VARCHAR(20) NOT NULL,
    store_uid VARCHAR(20) NOT NULL,
    cost INT NOT NULL,
    amount INT NOT NULL,
    buy_time DATETIME NOT NULL,
    PRIMARY KEY(customer_uid, product_uid, store_uid),
    FOREIGN KEY(customer_uid) REFERENCES online_customer(uid),
    FOREIGN KEY(product_uid) REFERENCES product(uid),
    FOREIGN KEY(store_uid) REFERENCES store(uid)
);