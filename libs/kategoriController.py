import mysql.connector

myDB = mysql.connector.connect(
    user = "root",
    password = "",
    database = "ecom",
    host = "localhost"
)

cursor = myDB.cursor()

def showAllKategori():
    query ="SELECT * FROM kategori"
    cursor = myDB.cursor(dictionary=True)
    cursor.execute(query)
    kategori = cursor.fetchall()

    return kategori

def showkategoriById(id):
    query = f"SELECT * FROM kategori WHERE IDKategori = {id}"
    cursor.execute(query)
    kategori = cursor.fetchone()

    return kategori

def addKategori(namaKategori):
    try:
        query ="""
        INSERT INTO kategori (nama_kategori) VALUES
        (%s)
        """
        
        values = (namaKategori,)
        
        cursor.execute(query, values)
        myDB.commit()
        print(f"Data kategori {namaKategori} berhasil di tambahkan")
        
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        myDB.rollback()
        
    finally:
        cursor.close()

def deleteKategori(id):
    try:
        query = f"""
        DELETE FROM kategori
        WHERE IDKategori = {id}
        """
        
        cursor.execute(query)
        myDB.commit()
        print(f"Data kategori dengan id {id} berhasil di hapus")
        
    except mysql.connector.Error as err:
        print(f"Error delete kategori: {err}")
        myDB.rollback()
        
    finally:
        cursor.close()


def updateKategori(id, nama):
    try:
        query = f"""
        UPDATE kategori
        SET nama_kategori = {nama}
        WHERE IDKategori = {id}
        """
        cursor.execute(query)
        myDB.commit()
        
        print(f"Data dengan id {id} berhasil di update")
        
    except mysql.connector.Error as err:
        print(f"Error updating kategori where id {id} err: {err}")
        myDB.rollback()
        
    finally:
        cursor.close()