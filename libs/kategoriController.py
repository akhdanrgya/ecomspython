import mysql.connector
from mysql.connector import errorcode

def connect_db():
    try:
        myDB_0501 = mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            database="ecom"
        )
        print("Connected to the database.")
        return myDB_0501
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        return None

myDB_0501 = connect_db()

if myDB_0501 is None:
    exit()

cursor_0501 = myDB_0501.cursor()

def showAllKategori():
    try:
        query_0501 = "SELECT * FROM kategori"
        cursor_0501 = myDB_0501.cursor(dictionary=True)
        cursor_0501.execute(query_0501)
        kategori_0501 = cursor_0501.fetchall()
        cursor_0501.close()
        return kategori_0501
    except mysql.connector.Error as err:
        print(f"Error fetching categories: {err}")
        return []

def showkategoriById(idk):
    try:
        query_0501 = f"SELECT * FROM kategori WHERE IDKategori = {idk}"
        cursor_0501.execute(query_0501)
        kategori_0501 = cursor_0501.fetchone()
        return kategori_0501
    except mysql.connector.Error as err:
        print(f"Error fetching category by ID: {err}")
        return None

def addKategori(namaKategori):
    try:
        query_0501 = """
        INSERT INTO kategori (nama_kategori) VALUES
        (%s)
        """
        values_0501 = (namaKategori,)
        cursor_0501.execute(query_0501, values_0501)
        myDB_0501.commit()
        print(f"Data kategori {namaKategori} berhasil ditambahkan")
    except mysql.connector.Error as err:
        print(f"Error adding category: {err}")
        myDB_0501.rollback()

def deleteKategori(idk):
    try:
        query_0501 = f"""
        DELETE FROM kategori
        WHERE IDKategori = {idk}
        """
        cursor_0501.execute(query_0501)
        myDB_0501.commit()
        print(f"Data kategori dengan id {idk} berhasil dihapus")
    except mysql.connector.Error as err:
        print(f"Error deleting category: {err}")
        myDB_0501.rollback()

def updateKategori(idK, nama):
    try:
        query_0501 = """
        UPDATE kategori
        SET nama_kategori = %s
        WHERE IDKategori = %s
        """
        value_0501 = (nama, idK)
        cursor_0501.execute(query_0501, value_0501)
        myDB_0501.commit()
        print(f"Data dengan id {idK} berhasil diupdate")
    except mysql.connector.Error as err:
        print(f"Error updating category where id {idK}: {err}")
        myDB_0501.rollback()

def searchKategori(val, key):
    try:
        kategori_0501 = showAllKategori()
        matchingKategori_0501 = [items for items in kategori_0501 if items[key] == val]
        if matchingKategori_0501:
            print("Kategori found:")
            for items in matchingKategori_0501:
                print(f"""
                      ID kategori   : {items['IDKategori']}
                      Nama Kategori : {items['nama_kategori']}
                      """)
            return matchingKategori_0501
        else:
            print("Data yang dicari tidak ada")
            return None
    except mysql.connector.Error as err:
        print(f"Error searching category: {err}")
        return None
