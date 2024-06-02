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

def showTransaction():
    query = """
    SELECT product.nama_produk, transaksi.jumlah, transaksi.total_harga
    FROM transaksi
    LEFT JOIN product ON transaksi.IDProduct = product.IDProduct;
    """
    try:
        cursor.execute(query)
        transaksi = cursor.fetchall()
        transaksiDict = []

        for items in transaksi:
            val = {
                'Nama Product' : items[0],
                'Jumlah' : items[1],
                'Total Harga' : items[2]
            }
            transaksiDict.append(val)
        
        return transaksiDict
    
    except mysql.connector.Error as err:
        print(f"Error : {err}")
