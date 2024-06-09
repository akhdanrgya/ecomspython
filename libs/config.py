import mysql.connector

def db():
    myDB_0501 = mysql.connector.connect(
        user="root",
        password="",
        host="localhost"
    )

    cursor_0501 = myDB_0501.cursor()
    
    cursor_0501.execute("CREATE DATABASE IF NOT EXISTS ecom;")
    myDB_0501.commit()
    cursor_0501.close()
    myDB_0501.close()

def tableKategori(cursor_0501):
    cursor_0501.execute("""
        CREATE TABLE IF NOT EXISTS kategori(
        IDKategori INT PRIMARY KEY AUTO_INCREMENT,
        nama_kategori VARCHAR(20)
        );
    """)

def tableProduct(cursor_0501):
    cursor_0501.execute("""
        CREATE TABLE IF NOT EXISTS product(
        IDProduct INT PRIMARY KEY AUTO_INCREMENT,
        IDKategori INT,
        nama_produk VARCHAR(255),
        harga INT,
        deskripsi VARCHAR(255),
        img VARCHAR(255),
        quantity INT,
        FOREIGN KEY (IDKategori) REFERENCES kategori(IDKategori)
    );
    """)

def tableTransaksi(cursor_0501):
    cursor_0501.execute("""
        CREATE TABLE IF NOT EXISTS transaksi(
        IDTransaksi INT PRIMARY KEY AUTO_INCREMENT,
        IDProduct INT,
        jumlah INT,
        total_harga INT,
        idKategori INT,
        FOREIGN KEY (IDProduct) REFERENCES product(IDProduct),
        FOREIGN KEY (IDKategori) REFERENCES kategori(IDKategori)
    );
    """)

def config():
    myDB_0501_use = mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="ecom"
    )
    
    cursor_0501 = myDB_0501_use.cursor()

    tableKategori(cursor_0501)
    tableProduct(cursor_0501)
    tableTransaksi(cursor_0501)

    myDB_0501_use.commit()
    cursor_0501.close()
    myDB_0501_use.close()

def runConfig():
    db()
    config()

if __name__ == "__main__":
    runConfig()
