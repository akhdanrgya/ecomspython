import mysql.connector

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

def showAllProductSorted():
    try:
        query = "SELECT * FROM product ORDER BY nama_produk"
        cursor = myDB.cursor(dictionary=True)
        cursor.execute(query)
        products = cursor.fetchall()
        return products
    except Exception as err:
        print(f"Error fetching data products: {err}")

def showProductById(id):
    try:
        query = f"""
        SELECT * FROM product
        WHERE IDProduct = {id}
        """
        
        cursor.execute(query)
        product = cursor.fetchone()
        
        return product
    except Exception as err:
        print(f"Data product dengan id {id} error : {err}")

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
        
    finally:
        cursor.close()

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
    
    return None

def searchProduct(nama_produk):
    products = showAllProduct()
    result = binarySearch(products, nama_produk, 'nama_produk')
    
    if result:
        print("Product found:", result)
        return result
    else:
        print("Product not found.")
        return None
