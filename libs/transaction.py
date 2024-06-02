import mysql.connector

myDB = mysql.connector.connect(
    user = "root",
    password = "",
    database = "ecom",
    host = "localhost"
)

cursor = myDB.cursor()

def buy(product, q, total):
    queryInsert = "INSERT INTO transaksi(IDProduct, jumlah, total_harga) VALUES (%s, %s, %s)"
    values = (product, q, total)

    try:
        cursor.execute(queryInsert, values)
        myDB.commit()
        print(f"Transaction Successfully ID Product {product}")
    
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        myDB.rollback()