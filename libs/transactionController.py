
import mysql.connector

# buat konekin database ke python
myDB_0501 = mysql.connector.connect(
    user = "root",
    password = "",
    database = "ecom",
    host = "localhost"
)

# buat eksekusi perintah di mysql
cursor_0501 = myDB_0501.cursor()

def kurangQuantity(id, newQ):
    try:
        query_0501 =f"""
        UPDATE product
        SET quantity = {newQ}
        WHERE IDProduct = {id}
        """
        
        cursor_0501.execute(query_0501)
        myDB_0501.commit()
    except mysql.connector.Error as err:
        print(f"product quantity error : {err}")
        myDB_0501.rollback()

def selectedQProduct(IDProduct):
    query_0501 = """SELECT quantity FROM product WHERE IDProduct = %s"""
    values_0501 = (IDProduct,)
    
    cursor_0501.execute(query_0501, values_0501)
    quantityProduct_0501 = cursor_0501.fetchone()

    return quantityProduct_0501[0]

def afterTransaction(IDProduct, q):
    quantity_0501 = selectedQProduct(IDProduct)
    final_0501 = quantity_0501 - q
    
    kurangQuantity(IDProduct, final_0501)

def buy(product, q, total, kategori):
    queryInsert_0501 = "INSERT INTO transaksi(IDProduct, jumlah, total_harga, IDKategori) VALUES (%s, %s, %s, %s)"
    values_0501 = (product, q, total, kategori)

    # buat debugging jadi tau apa yang error
    try:
        cursor_0501.execute(queryInsert_0501, values_0501)
        myDB_0501.commit()
        print(f"Transaction Successfully ID Product {product}")
        afterTransaction(product, q)
    
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        myDB_0501.rollback()

def showTransaction():
    query_0501 = """
    SELECT transaksi.IDTransaksi, product.nama_produk, transaksi.jumlah, transaksi.total_harga, transaksi.IDKategori
    FROM transaksi
    LEFT JOIN product ON transaksi.IDProduct = product.IDProduct;
    """
    try:
        cursor_0501.execute(query_0501)
        transaksi_0501 = cursor_0501.fetchall()
        transaksiDict_0501 = []

        for items in transaksi_0501:
            val_0501 = {
                'IDTransaksi' : items[0],
                'Nama Product' : items[1],
                'Jumlah' : items[2],
                'Total Harga' : items[3],
                'IDKategori' : items[4]
            }
            transaksiDict_0501.append(val_0501)
        
        if not transaksiDict_0501:
            print("Tidak ada transaksi")
        
        return transaksiDict_0501
    
    except mysql.connector.Error as err:
        print(f"Error : {err}")

def searchTransactions(key, val):
    transaction_0501 = showTransaction()
    matchingTransaction_0501 = [items for items in transaction_0501 if items[key] == val]

    if matchingTransaction_0501:
        print("Transaction found:")
        for items in matchingTransaction_0501:
            print(f"""
            ID Transaction      : {items['IDTransaksi']}
            Nama Product        : {items['Nama Product']}
            Jumlah              : {items['Jumlah']}
            Total Harga         : {items['Total Harga']}
            ID Kategori         : {items['IDKategori']}
            """)
        return matchingTransaction_0501
    else:
        print("Product not found.")

def showKategoriTransaksiCounts():
    query_0501 = """
    SELECT k.nama_kategori, COUNT(t.IDTransaksi) as jumlah_transaksi
    FROM kategori k
    LEFT JOIN transaksi t ON k.IDKategori = t.IDKategori
    GROUP BY k.nama_kategori
    """
    cursor_0501 = myDB_0501.cursor(dictionary=True)
    cursor_0501.execute(query_0501)
    results_0501 = cursor_0501.fetchall()
    return results_0501

def showJumlahYangHabis():
    query_0501 = """
    SELECT k.nama_kategori, COUNT(t.IDTransaksi) as jumlah_transaksi, SUM(t.jumlah) as total_terjual
    FROM kategori k
    LEFT JOIN transaksi t ON k.IDKategori = t.IDKategori
    WHERE t.jumlah > 0
    GROUP BY k.nama_kategori
    """
    cursor_0501 = myDB_0501.cursor(dictionary=True)
    cursor_0501.execute(query_0501)
    results_0501 = cursor_0501.fetchall()
    return results_0501


def showKeuntunganPerKategori():
    query_0501 = """
    SELECT k.nama_kategori, SUM(t.total_harga) as keuntungan
    FROM kategori k
    LEFT JOIN product p ON k.IDKategori = p.IDKategori
    LEFT JOIN transaksi t ON p.IDProduct = t.IDProduct
    GROUP BY k.nama_kategori
    """
    cursor_0501 = myDB_0501.cursor(dictionary=True)
    cursor_0501.execute(query_0501)
    results_0501 = cursor_0501.fetchall()
    return results_0501