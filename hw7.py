import sqlite3

def create_connection(db_file):
    connection = None
    try:
        connection = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    return connection



db_name = 'hw.db'


sql_create_products_table = '''
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    price FLOAT(10, 2) NOT NULL DEFAULT 0.0,
    quantity INT(10, 2) NOT NULL DEFAULT 0 ,
    product_title TEXT VARCHAR(200) NOT NULL
    )
'''

def create_table(db_file, create_table_sql):
    try:
        with sqlite3.connect(db_file) as connection:
            cursor = connection.cursor()
            cursor.execute(create_table_sql)
    except sqlite3.Error as e:
        print(e)


def insert_product(db_file, product):
    sql = '''INSERT INTO products 
    (product_title, price ,quantity) 
    VALUES (?, ?, ?)'''
    try:
        with sqlite3.connect(db_file) as connection:
            cursor = connection.cursor()
            cursor.execute(sql,product )
            connection.commit()
    except sqlite3.Error as e:
        print(e)

def update_product_quantity_by_id(db_file, product_quantity,product_id):
    sql = '''UPDATE products SET quantity = ? WHERE id = ?'''
    try:
        with sqlite3.connect(db_file) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, (product_quantity,product_id))
    except sqlite3.Error as e:
        print(e)

def update_product_price_by_id(db_file, product_price,product_id):
    sql = '''UPDATE products SET price = ? WHERE id = ?'''
    try:
        with sqlite3.connect(db_file) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, (product_price,product_id))
    except sqlite3.Error as e:
        print(e)


def delete_product(db_file, product_id):
    sql = '''DELETE FROM products WHERE id = ?'''
    try:
        with sqlite3.connect(db_file) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, (product_id,))
            connection.commit()
            print("deleted succesfully")
    except sqlite3.Error as e:
        print(e)

def select_all_products(db_file):
    sql = '''SELECT * FROM products'''
    try:
        with sqlite3.connect(db_file) as connection:
            cursor = connection.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except sqlite3.Error as e:
        print(e)

def select_product_by_price(db_file, price_limit):
    sql = '''SELECT * FROM products WHERE price <= ?'''
    try:
        with sqlite3.connect(db_file) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, (price_limit,))
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except sqlite3.Error as e:
        print(e)


def select_product_by_title(db_file):
    sql = '''SELECT * FROM products WHERE product_title LIKE '%brown%' '''
    try:
        with sqlite3.connect(db_file) as connection:
            cursor = connection.cursor()
            cursor.execute(sql,)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except sqlite3.Error as e:
        print(e)

my_conn = create_connection(db_name)
if my_conn is not None:
    print('Successfully connected to database')

    # create_table(db_name, sql_create_products_table)

    # insert_product(db_name,("greenphone", 2000,100))
    # insert_product(db_name,("bluephone", 2500,121))
    # insert_product(db_name,("yellowphone", 3900,156))
    # insert_product(db_name,("purephone", 3200,189))
    # insert_product(db_name,("redphone", 4600,198))
    # insert_product(db_name,("brownphone", 6700,101))
    # insert_product(db_name,("whithephone", 8400,134))
    # insert_product(db_name,("blackphone", 9300,123))
    # insert_product(db_name,("smartphone", 1200,178))
    # insert_product(db_name,("rosephone", 7600,1000))
    # insert_product(db_name,("noutphone", 3500,104))
    # insert_product(db_name,("telephone", 5400,465))
    # insert_product(db_name,("pipphone", 1000,345))
    # insert_product(db_name,("iphone", 9900,234))
    # insert_product(db_name,("snowphone", 8700,789))
    # update_product_price_by_id(db_name,2500, 2)
    # update_product_quantity_by_id(db_name,245,6)
    select_product_by_price(db_name,5000)
    select_all_products(db_name)
    select_product_by_title(db_name)
    delete_product(db_name,7)



