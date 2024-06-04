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

def showkategoriById(idk):
    query = f"SELECT * FROM kategori WHERE IDKategori = {idk}"
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
        


def deleteKategori(idk):
    try:
        query = f"""
        DELETE FROM kategori
        WHERE IDKategori = {idk}
        """
        
        cursor.execute(query)
        myDB.commit()
        print(f"Data kategori dengan id {idk} berhasil di hapus")
        
    except mysql.connector.Error as err:
        print(f"Error delete kategori: {err}")
        myDB.rollback()


def updateKategori(idK, nama):
    try:
        query = """
        UPDATE kategori
        SET nama_kategori = %s
        WHERE IDKategori = %s
        """
        value = (nama, idK)
        
        cursor.execute(query, value)
        myDB.commit()
        
        print(f"Data dengan id {idK} berhasil di update")
        
    except mysql.connector.Error as err:
        print(f"Error updating kategori where id {idK} err: {err}")
        myDB.rollback()

def searchKategori(val, key):
    kategori = showAllKategori()

    mathcingKategori = [items for items in kategori if items[key] == val]

    if mathcingKategori:
        print("Kategori found:")
        for items in mathcingKategori:
            print(f"""
                  ID kategori   : {items['IDKategori']}
                  Nama Kategori : {items['nama_kategori']}
                  """)
            return mathcingKategori
    else:
        print("Data yang dicari tidak ada")
        return None
