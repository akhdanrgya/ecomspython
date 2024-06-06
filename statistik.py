import matplotlib.pyplot as plt
import random
from libs.kategoriController import *
from libs.transactionController import *
from libs.productController import *

def generate_random_colors(num_colors):
    colors_0501 = []
    for _ in range(num_colors):
        r = random.randint(0, 255) / 255
        g = random.randint(0, 255) / 255
        b = random.randint(0, 255) / 255
        colors_0501.append((r, g, b))
    return colors_0501

def pembelianKategori():
    kategori_data_0501 = showKategoriTransaksiCounts()
    
    namaKategori_0501 = [item['nama_kategori'] for item in kategori_data_0501]
    counts_0501 = [item['jumlah_transaksi'] for item in kategori_data_0501]
    
    base_colors_0501 = generate_random_colors(len(namaKategori_0501))
    bar_colors_0501 = (base_colors_0501 * ((len(namaKategori_0501) // len(base_colors_0501)) + 1))[:len(namaKategori_0501)]
    
    fig, ax = plt.subplots()

    bar_labels_0501 = namaKategori_0501

    ax.bar(namaKategori_0501, counts_0501, label=bar_labels_0501, color=bar_colors_0501)

    ax.set_ylabel('Jumlah Transaksi')
    ax.set_title('Statistik Transaksi Berdasarkan Kategori Produk')
    ax.legend(title='Kategori')

    plt.show()

def plotKategoriTerjual():
    kategori_data_0501 = showJumlahYangHabis()
    
    if not kategori_data_0501:
        print("Tidak ada kategori dengan jumlah terjual.")
        return
    
    namaKategori_0501 = [item['nama_kategori'] for item in kategori_data_0501]
    total_terjual_0501 = [item['total_terjual'] for item in kategori_data_0501]
    bar_colors_0501 = generate_random_colors(len(namaKategori_0501))

    fig, ax = plt.subplots()

    ax.bar(namaKategori_0501, total_terjual_0501, label=namaKategori_0501, color=bar_colors_0501)

    ax.set_xlabel('Kategori')
    ax.set_ylabel('Jumlah Produk Terjual')
    ax.set_title('Statistik Kategori Produk dengan Penjualan')
    ax.legend(title='Kategori')

    plt.show()

def plotKetersediaanProduk():
    produkData_0501 = showAllProduct2()
    
    if not produkData_0501:
        print("Tidak ada data")
        return
    
    namaProduk_0501 = [item['nama_produk'] for item in produkData_0501]
    jumlahProduk_0501 = [item['quantity'] for item in produkData_0501]
    bar_colors_0501 = generate_random_colors(len(namaProduk_0501))

    fig, ax = plt.subplots()

    ax.bar(namaProduk_0501, jumlahProduk_0501, label=namaProduk_0501, color=bar_colors_0501)

    ax.set_xlabel('Nama Produk')
    ax.set_ylabel('Jumlah Produk Tersedia')
    ax.set_title('Statistik Jumlah Produk Tersedia')
    ax.legend(title='Product Quantity')

    plt.show()

def plotKeuntungan():
    keuntungan_data_0501 = showKeuntunganPerKategori()
    
    if not keuntungan_data_0501:
        print("Tidak ada data keuntungan untuk kategori apapun.")
        return
    
    namaKategori_0501 = [item['nama_kategori'] for item in keuntungan_data_0501]
    total_keuntungan_0501 = [item['keuntungan'] for item in keuntungan_data_0501]
    bar_colors_0501 = generate_random_colors(len(namaKategori_0501))

    fig, ax = plt.subplots()

    ax.bar(namaKategori_0501, total_keuntungan_0501, label=namaKategori_0501, color=bar_colors_0501)

    ax.set_xlabel('Kategori')
    ax.set_ylabel('Keuntungan (Rp)')
    ax.set_title('Statistik Keuntungan Berbagai Kategori Produk')
    ax.legend(title='Kategori')

    plt.show()
