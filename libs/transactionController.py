
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

def buy(product, q, total, kategori):
    queryInsert = "INSERT INTO transaksi(IDProduct, jumlah, total_harga, IDKategori) VALUES (%s, %s, %s, %s)"
    values = (product, q, total, kategori)

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
    SELECT transaksi.IDTransaksi, product.nama_produk, transaksi.jumlah, transaksi.total_harga, transaksi.IDKategori
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
                'Total Harga' : items[3],
                'IDKategori' : items[4]
            }
            transaksiDict.append(val)
        
        if not transaksiDict:
            print("Tidak ada transaksi")
        
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
            ID Kategori         : {items['IDKategori']}
            """)
        return matchingTransaction
    else:
        print("Product not found.")

def showKategoriTransaksiCounts():
    query = """
    SELECT k.nama_kategori, COUNT(t.IDTransaksi) as jumlah_transaksi
    FROM kategori k
    LEFT JOIN transaksi t ON k.IDKategori = t.IDKategori
    GROUP BY k.nama_kategori
    """
    cursor = myDB.cursor(dictionary=True)
    cursor.execute(query)
    results = cursor.fetchall()
    return results

def showJumlahYangHabis():
    query = """
    SELECT k.nama_kategori, COUNT(t.IDTransaksi) as jumlah_transaksi, SUM(t.jumlah) as total_terjual
    FROM kategori k
    LEFT JOIN transaksi t ON k.IDKategori = t.IDKategori
    WHERE t.jumlah > 0
    GROUP BY k.nama_kategori
    """
    cursor = myDB.cursor(dictionary=True)
    cursor.execute(query)
    results = cursor.fetchall()
    return results


def showKeuntunganPerKategori():
    query = """
    SELECT k.nama_kategori, SUM(t.total_harga) as keuntungan
    FROM kategori k
    LEFT JOIN product p ON k.IDKategori = p.IDKategori
    LEFT JOIN transaksi t ON p.IDProduct = t.IDProduct
    GROUP BY k.nama_kategori
    """
    cursor = myDB.cursor(dictionary=True)
    cursor.execute(query)
    results = cursor.fetchall()
    return results