import mysql.connector

myDB_0501 = mysql.connector.connect(
    user = "root",
    password = "",
    host = "localhost"
)

cursor_0501 = myDB_0501.cursor()\

def config():
    cursor_0501.execute("""
                        CREATE DATABASE IF NOT EXISTS ecom;
    USE ecom;

    CREATE TABLE IF NOT EXISTS kategori(
        IDKategori INT PRIMARY KEY AUTO_INCREMENT,
        nama_kategori VARCHAR(20)
    );

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

    CREATE TABLE IF NOT EXISTS transaksi(
        IDTransaksi INT PRIMARY KEY AUTO_INCREMENT,
        IDProduct INT,
        jumlah INT,
        total_harga INT,
        FOREIGN KEY (IDProduct) REFERENCES product(IDProduct)
    );

    """)