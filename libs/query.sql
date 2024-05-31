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

CREATE TABLE customer(
	IDCustomer INT PRIMARY KEY AUTO_INCREMENT,
    nama_depan VARCHAR(30),
    nama_belakang VARCHAR(30),
    username VARCHAR(30),
    password VARCHAR(30),
    alamat VARCHAR(255)
);

CREATE TABLE admin(
	IDAdmin INT PRIMARY KEY auto_increment,
    adminName VARCHAR(30),
    password VARCHAR(30)
);

INSERT INTO kategori(nama_kategori) VALUES
	('Makanan'),
    ('Minuman'),
    ('Pakaian');

INSERT INTO product(IDKategori, nama_produk, harga, deskripsi, img, quantity) VALUES
	(1, 'Dimsum', 4000, 'ENAK BANGET COK', 'dimsum.png', 100);

