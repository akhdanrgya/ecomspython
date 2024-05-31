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
        
    finally:
        cursor.close()

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
        
    finally:
        cursor.close()

def upadteProduct(id, IDkategori, nama, harga, desk, img, q):
    try:
        query = f"""
        UPDATE product
        SET IDKategori = {IDkategori}, nama_produk = {nama}, harga {harga}, deskripsi = {desk}, img = {img}, quantity = {q}
        WHERE IDProduct = {id}
        """
        cursor.execute(query)
        print(f"Data product dengan id {id} berhasil di update")
        myDB.commit()
        
    except mysql.connector.Error as err:
        print(f"Error updating Product where id : {id} err : {err}")
        myDB.rollback()
    
    finally:
        cursor.close()

def showAllProduct():
    try:
        query = f"""
        SELECT * FROM product
        """
        
        cursor = myDB.cursor(dictionary=True)
        cursor.execute(query)
        product = cursor.fetchall()
        
        return product
    except Exception as err:
        print(f"Error data product err : {err}")

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