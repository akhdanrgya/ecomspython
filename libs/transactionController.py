
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
    SELECT transaksi.IDTransaksi, product.nama_produk, transaksi.jumlah, transaksi.total_harga
    FROM transaksi
    LEFT JOIN product ON transaksi.IDProduct = product.IDProduct;
    """
    try:
        cursor.execute(query)
        transaksi = cursor.fetchall()
        transaksiDict = []

        for items in transaksi:
            val = {
                'IDTransaksi' : items[0],
                'Nama Product' : items[1],
                'Jumlah' : items[2],
                'Total Harga' : items[3]
            }
            transaksiDict.append(val)
        
        return transaksiDict
    
    except mysql.connector.Error as err:
        print(f"Error : {err}")

def searchTransactions(key, val):
    transaction = showTransaction()
    matchingTransaction = [items for items in transaction if items[key] == val]

    if matchingTransaction:
        print("Transaction found:")
        for items in matchingTransaction:
            print(f"""
            ID Transaction      : {items['IDTransaksi']}
            Nama Product        : {items['Nama Product']}
            Jumlah              : {items['Jumlah']}
            Total Harga         : {items['Total Harga']}
            """)
        return matchingTransaction
    else:
        print("Product not found.")