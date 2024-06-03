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

def dynamicUpdateProduct(idp, IDkategori, nama, harga, desk, img, q):
    try:
        # List of fields to update and their corresponding values
        fields = []
        values = []
        
        # Check each parameter, add to fields and values if not None
        if IDkategori is not None:
            fields.append("IDKategori = %s")
            values.append(IDkategori)
        if nama is not None:
            fields.append("nama_produk = %s")
            values.append(nama)
        if harga is not None:
            fields.append("harga = %s")
            values.append(harga)
        if desk is not None:
            fields.append("deskripsi = %s")
            values.append(desk)
        if img is not None:
            fields.append("img = %s")
            values.append(img)
        if q is not None:
            fields.append("quantity = %s")
            values.append(q)
        
        # If no fields are provided, raise an error
        if not fields:
            print("No fields to update!")
            return

        # Create the query string
        query = f"""
        UPDATE product
        SET {', '.join(fields)}
        WHERE IDProduct = %s
        """
        values.append(idp)
        
        cursor.execute(query, tuple(values))
        print(f"Data product dengan id {idp} berhasil di update")
        myDB.commit()
        
    except mysql.connector.Error as err:
        print(f"Error updating Product where id: {idp}, err: {err}")
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

def searchProductsByQuantity(quantity):
    products = showAllProduct2()
    
    matching_products = [product for product in products if product['quantity'] == quantity]
    
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

def searchProductsByID(ProdID):
    products = showAllProduct2()
    
    matching_products = [product for product in products if product['IDProduct'] == ProdID]
    
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
        print("Data yang dicari tidak ada.")
        return None