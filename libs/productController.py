import mysql.connector
from tkinter import filedialog
import os

myDB = mysql.connector.connect(
    user = "root",
    password = "",
    database = "ecom",
    host = "localhost"
)

cursor = myDB.cursor()

def addProduct(idkategori, nama, harga, desc, img, q):
    query = """
    INSERT INTO product (IDKategori, nama_produk, harga, deskripsi, img, quantity) VALUES (%s, %s, %s, %s, %s, %s)
    """
    values = (idkategori, nama, harga, desc, img, q)
    
    try:
        cursor.execute(query, values)
        myDB.commit()
        print("Product added successfully.")
        
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        myDB.rollback()

def deleteProduct(id):
    try:
        query = f"""
        DELETE FROM product
        WHERE IDProduct = {id}
        """
        
        cursor.execute(query)
        myDB.commit()
        print(f"Produk dengan id {id} berhasil di hapus")
        
    except mysql.connector.Error as err:
        print(f"Error deleting product: {err}")
        myDB.rollback()



def updateProduct(idp, IDkategori, nama, harga, desk, img, q):
    try:
        query = """
        UPDATE product
        SET IDKategori = %s, nama_produk = %s, harga = %s, deskripsi = %s, img = %s, quantity = %s
        WHERE IDProduct = %s
        """
        cursor.execute(query, (IDkategori, nama, harga, desk, img, q, idp))
        print(f"Data product dengan id {idp} berhasil di update")
        myDB.commit()
        
    except mysql.connector.Error as err:
        print(f"Error updating Product where id : {idp} err : {err}")
        myDB.rollback()


def showAllProduct():
    try:
        query = f"""
        SELECT * FROM product
        """
        
        cursor.execute(query)
        product = cursor.fetchall()
        
        return product
    except Exception as err:
        print(f"Error data product err : {err}")

def showAllProduct2():
    try:
        query = "SELECT * FROM product"
        cursor.execute(query)
        products = cursor.fetchall()
        
        product_dicts = []
        for product in products:
            product_dict = {
                'IDProduct': product[0],
                'IDKategori': product[1],
                'nama_produk': product[2],
                'harga': product[3],
                'deskripsi': product[4],
                'img': product[5],
                'quantity': product[6]
            }
            product_dicts.append(product_dict)
        
        myDB.commit()
        
        if not product_dicts:
            print("Tidak ada product")
        
        return product_dicts
    
    except Exception as err:
        print(f"Error fetching products: {err}")


def showAllProductSorted():
    try:
        query = "SELECT * FROM product ORDER BY nama_produk"
        cursor = myDB.cursor(dictionary=True)
        cursor.execute(query)
        products = cursor.fetchall()
        return products
    except Exception as err:
        print(f"Error fetching data products: {err}")

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
        


def binarySearch(arr, target, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        midVal = arr[mid][key]

        if midVal < target:
            low = mid + 1
        elif midVal > target:
            high = mid - 1
        else:
            return arr[mid]

def searchProduct(value, key):
    products = showAllProductSorted()
    result = binarySearch(products, value, key)
    
    if result:
        print("Product found:")
        print(f"""
        ID Product    : {result['IDProduct']}
        ID Kategori   : {result['IDKategori']}
        Nama Product  : {result['nama_produk']}
        Harga         : {result['harga']}
        Deskripsi     : {result['deskripsi']}
        Gambar        : {result['img']}
        Quantity      : {result['quantity']}
        """)
    else:
        print("Product not found.")

def searchProduct2(val, key):
    products = showAllProduct2()
    
    matching_products = [product for product in products if product[key] == val]
    
    if matching_products:
        print("Products found:")
        for product in matching_products:
            print(f"""
            ID Product    : {product['IDProduct']}
            ID Kategori   : {product['IDKategori']}
            Nama Product  : {product['nama_produk']}
            Harga         : {product['harga']}
            Deskripsi     : {product['deskripsi']}
            Gambar        : {product['img']}
            Quantity      : {product['quantity']}
            """)
        return matching_products
    else:
        print("No products found with the specified quantity.")
        return None

