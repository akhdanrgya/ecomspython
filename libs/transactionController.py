import mysql.connector

# buat konekin database ke python
myDB = mysql.connector.connect(
    user = "root",
    password = "",
    database = "ecom",
    host = "localhost"
)

# buat eksekusi perintah di mysql
cursor = myDB.cursor()

def selectedProduct(IDProduct):
    query = """SELECT quantity FROM product WHERE IDProduct = %s"""
    values = (IDProduct,)
    
    cursor.execute(query, values)
    quantityProduct = cursor.fetchone()

    return quantityProduct

def buy(product, q, total):
    queryInsert = "INSERT INTO transaksi(IDProduct, jumlah, total_harga) VALUES (%s, %s, %s)"
    values = (product, q, total)

    # buat debugging jadi tau apa yang error
    try:
        cursor.execute(queryInsert, values)
        myDB.commit()
        print(f"Transaction Successfully ID Product {product}")
        
        quantityProduct = selectedProduct(product)
        kurang = quantityProduct - q

        print(kurang)
    
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
