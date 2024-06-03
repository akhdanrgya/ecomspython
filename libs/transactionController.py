
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

def kurangQuantity(id, newQ):
    try:
        query =f"""
        UPDATE product
        SET quantity = {newQ}
        WHERE IDProduct = {id}
        """
        
        cursor.execute(query)
        myDB.commit()
    except mysql.connector.Error as err:
        print(f"product quantity error : {err}")
        myDB.rollback()

def selectedQProduct(IDProduct):
    query = """SELECT quantity FROM product WHERE IDProduct = %s"""
    values = (IDProduct,)
    
    cursor.execute(query, values)
    quantityProduct = cursor.fetchone()

    return quantityProduct[0]

def afterTransaction(IDProduct, q):
    quantity = selectedQProduct(IDProduct)
    final = quantity - q
    
    kurangQuantity(IDProduct, final)

def buy(product, q, total):
    queryInsert = "INSERT INTO transaksi(IDProduct, jumlah, total_harga) VALUES (%s, %s, %s)"
    values = (product, q, total)

    # buat debugging jadi tau apa yang error
    try:
        cursor.execute(queryInsert, values)
        myDB.commit()
        print(f"Transaction Successfully ID Product {product}")
        afterTransaction(product, q)
    
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
