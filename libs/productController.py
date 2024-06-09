import mysql.connector
from tkinter import filedialog, Tk
import os
import shutil

myDB_0501 = mysql.connector.connect(
    user = "root",
    password = "",
    database = "ecom",
    host = "localhost"
)

cursor_0501 = myDB_0501.cursor()

def addProduct(idkategori, nama, harga, desc, img, q):
    query_0501 = """
    INSERT INTO product (IDKategori, nama_produk, harga, deskripsi, img, quantity) VALUES (%s, %s, %s, %s, %s, %s)
    """
    values_0501 = (idkategori, nama, harga, desc, img, q)
    
    try:
        cursor_0501.execute(query_0501, values_0501)
        myDB_0501.commit()
        print("Product added successfully.")
        
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        myDB_0501.rollback()

def deleteProduct(id):
    try:
        query_0501 = f"""
        DELETE FROM product
        WHERE IDProduct = {id}
        """
        
        cursor_0501.execute(query_0501)
        myDB_0501.commit()
        print(f"Produk dengan id {id} berhasil di hapus")
        
    except mysql.connector.Error as err:
        print(f"Error deleting product: {err}")
        myDB_0501.rollback()



def updateProduct(idp, IDkategori, nama, harga, desk, img, q):
    try:
        query_0501 = """
        UPDATE product
        SET IDKategori = %s, nama_produk = %s, harga = %s, deskripsi = %s, img = %s, quantity = %s
        WHERE IDProduct = %s
        """
        cursor_0501.execute(query_0501, (IDkategori, nama, harga, desk, img, q, idp))
        print(f"Data product dengan id {idp} berhasil di update")
        myDB_0501.commit()
        
    except mysql.connector.Error as err:
        print(f"Error updating Product where id : {idp} err : {err}")
        myDB_0501.rollback()


def showAllProduct():
    try:
        query_0501 = f"""
        SELECT * FROM product
        """
        
        cursor_0501.execute(query_0501)
        product_0501 = cursor_0501.fetchall()
        
        return product_0501
    except Exception as err:
        print(f"Error data product err : {err}")

def showAllProduct2():
    try:
        query_0501 = "SELECT * FROM product"
        cursor_0501.execute(query_0501)
        products_0501 = cursor_0501.fetchall()
        
        product_dicts_0501 = []
        for product in products_0501:
            product_dict_0501 = {
                'IDProduct': product[0],
                'IDKategori': product[1],
                'nama_produk': product[2],
                'harga': product[3],
                'deskripsi': product[4],
                'img': product[5],
                'quantity': product[6]
            }
            product_dicts_0501.append(product_dict_0501)
        
        myDB_0501.commit()
        
        return product_dicts_0501
    
    except Exception as err:
        print(f"Error fetching products: {err}")


def showAllProductSorted():
    try:
        query_0501 = "SELECT * FROM product ORDER BY nama_produk"
        cursor_0501 = myDB_0501.cursor(dictionary=True)
        cursor_0501.execute(query_0501)
        products_0501 = cursor_0501.fetchall()
        return products_0501
    except Exception as err:
        print(f"Error fetching data products: {err}")

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
        


def binarySearch(arr, target, key):
    low_0501 = 0
    high_0501 = len(arr) - 1

    while low_0501 <= high_0501:
        mid_0501 = (low_0501 + high_0501) // 2
        midVal_0501 = arr[mid_0501][key]

        if midVal_0501 < target:
            low_0501 = mid_0501 + 1
        elif midVal_0501 > target:
            high_0501 = mid_0501 - 1
        else:
            return arr[mid_0501]

def searchProduct(value, key):
    products_0501 = showAllProductSorted()
    result_0501 = binarySearch(products_0501, value, key)
    
    if result_0501:
        print("Product found:")
        print(f"""
        ID Product    : {result_0501['IDProduct']}
        ID Kategori   : {result_0501['IDKategori']}
        Nama Product  : {result_0501['nama_produk']}
        Harga         : {result_0501['harga']}
        Deskripsi     : {result_0501['deskripsi']}
        Gambar        : {result_0501['img']}
        Quantity      : {result_0501['quantity']}
        """)
    else:
        print("Product not found.")

def searchProduct2(val, key):
    products_0501 = showAllProduct2()
    
    matching_products_0501 = [product for product in products_0501 if product[key] == val]
    
    if matching_products_0501:
        print("Products found:")
        for product in matching_products_0501:
            print(f"""
            ID Product    : {product['IDProduct']}
            ID Kategori   : {product['IDKategori']}
            Nama Product  : {product['nama_produk']}
            Harga         : {product['harga']}
            Deskripsi     : {product['deskripsi']}
            Gambar        : {product['img']}
            Quantity      : {product['quantity']}
            """)
        return matching_products_0501
    else:
        print("No products found with the specified quantity.")
        return None