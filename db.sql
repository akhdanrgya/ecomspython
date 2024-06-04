create database ecom;
use ecom;

CREATE TABLE kategori(
	IDKategori INT PRIMARY KEY auto_increment,
    nama_kategori VARCHAR(20)
);

CREATE TABLE product(
	IDProduct INT PRIMARY KEY AUTO_INCREMENT,
    IDKategori INT,
    nama_produk VARCHAR(255),
    harga int,
    deskripsi VARCHAR(255),
	img VARCHAR(255),
    quantity INT,
    
    FOREIGN KEY(IDKategori) REFERENCES kategori(IDKategori)
);

CREATE TABLE transaksi(
	IDTransaksi INT PRIMARY KEY auto_increment,
    IDProduct INT,
    jumlah INT,
    total_harga INT
);