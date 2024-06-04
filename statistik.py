import matplotlib.pyplot as plt
import random
from libs.kategoriController import *
from libs.transactionController import *
from libs.productController import *

def generate_random_colors(num_colors):
    colors = []
    for _ in range(num_colors):
        r = random.randint(0, 255) / 255
        g = random.randint(0, 255) / 255
        b = random.randint(0, 255) / 255
        colors.append((r, g, b))
    return colors

def pembelianKategori():
    kategori_data = showKategoriTransaksiCounts()
    
    namaKategori = [item['nama_kategori'] for item in kategori_data]
    counts = [item['jumlah_transaksi'] for item in kategori_data]
    
    base_colors = generate_random_colors(len(namaKategori))
    bar_colors = (base_colors * ((len(namaKategori) // len(base_colors)) + 1))[:len(namaKategori)]
    
    fig, ax = plt.subplots()

    bar_labels = namaKategori

    ax.bar(namaKategori, counts, label=bar_labels, color=bar_colors)

    ax.set_ylabel('Jumlah Transaksi')
    ax.set_title('Statistik Transaksi Berdasarkan Kategori Produk')
    ax.legend(title='Kategori')

    plt.show()

def plotKategoriTerjual():
    kategori_data = showJumlahYangHabis()
    
    if not kategori_data:
        print("Tidak ada kategori dengan jumlah terjual.")
        return
    
    namaKategori = [item['nama_kategori'] for item in kategori_data]
    total_terjual = [item['total_terjual'] for item in kategori_data]
    bar_colors = generate_random_colors(len(namaKategori))

    fig, ax = plt.subplots()

    ax.bar(namaKategori, total_terjual, label=namaKategori, color=bar_colors)

    ax.set_xlabel('Kategori')
    ax.set_ylabel('Jumlah Produk Terjual')
    ax.set_title('Statistik Kategori Produk dengan Penjualan')
    ax.legend(title='Kategori')

    plt.show()

def plotKetersediaanProduk():
    produkData = showAllProduct2()
    
    if not produkData:
        print("Tidak ada data")
        return
    
    namaProduk = [item['nama_produk'] for item in produkData]
    jumlahProduk = [item['quantity'] for item in produkData]
    bar_colors = generate_random_colors(len(namaProduk))

    fig, ax = plt.subplots()

    ax.bar(namaProduk, jumlahProduk, label=namaProduk, color=bar_colors)

    ax.set_xlabel('Nama Produk')
    ax.set_ylabel('Jumlah Produk Tersedia')
    ax.set_title('Statistik Jumlah Produk Tersedia')
    ax.legend(title='Product Quantity')

    plt.show()

def plotKeuntungan():
    keuntungan_data = showKeuntunganPerKategori()
    
    if not keuntungan_data:
        print("Tidak ada data keuntungan untuk kategori apapun.")
        return
    
    namaKategori = [item['nama_kategori'] for item in keuntungan_data]
    total_keuntungan = [item['keuntungan'] for item in keuntungan_data]
    bar_colors = generate_random_colors(len(namaKategori))

    fig, ax = plt.subplots()

    ax.bar(namaKategori, total_keuntungan, label=namaKategori, color=bar_colors)

    ax.set_xlabel('Kategori')
    ax.set_ylabel('Keuntungan (Rp)')
    ax.set_title('Statistik Keuntungan Berbagai Kategori Produk')
    ax.legend(title='Kategori')

    plt.show()
