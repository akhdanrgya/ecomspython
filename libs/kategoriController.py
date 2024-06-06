import mysql.connector

myDB_0501 = mysql.connector.connect(
    user = "root",
    password = "",
    database = "ecom",
    host = "localhost"
)

cursor_0501 = myDB_0501.cursor()

def showAllKategori():
    query_0501 ="SELECT * FROM kategori"
    cursor_0501 = myDB_0501.cursor(dictionary=True)
    cursor_0501.execute(query_0501)
    kategori_0501 = cursor_0501.fetchall()

    return kategori_0501

def showkategoriById(idk):
    query_0501 = f"SELECT * FROM kategori WHERE IDKategori = {idk}"
    cursor_0501.execute(query_0501)
    kategori_0501 = cursor_0501.fetchone()

    return kategori_0501

def addKategori(namaKategori):
    try:
        query_0501 ="""
        INSERT INTO kategori (nama_kategori) VALUES
        (%s)
        """
        
        values_0501 = (namaKategori,)
        
        cursor_0501.execute(query_0501, values_0501)
        myDB_0501.commit()
        print(f"Data kategori {namaKategori} berhasil di tambahkan")
        
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        myDB_0501.rollback()
        


def deleteKategori(idk):
    try:
        query_0501 = f"""
        DELETE FROM kategori
        WHERE IDKategori = {idk}
        """
        
        cursor_0501.execute(query_0501)
        myDB_0501.commit()
        print(f"Data kategori dengan id {idk} berhasil di hapus")
        
    except mysql.connector.Error as err:
        print(f"Error delete kategori: {err}")
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
        
        print(f"Data dengan id {idK} berhasil di update")
        
    except mysql.connector.Error as err:
        print(f"Error updating kategori where id {idK} err: {err}")
        myDB_0501.rollback()

def searchKategori(val, key):
    kategori_0501 = showAllKategori()

    mathcingKategori_0501 = [items for items in kategori_0501 if items[key] == val]

    if mathcingKategori_0501:
        print("Kategori found:")
        for items in mathcingKategori_0501:
            print(f"""
                  ID kategori   : {items['IDKategori']}
                  Nama Kategori : {items['nama_kategori']}
                  """)
            return mathcingKategori_0501
    else:
        print("Data yang dicari tidak ada")
        return None
