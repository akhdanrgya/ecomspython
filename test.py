from libs.productController import *
from libs.kategoriController import *

def main():
    print("<< main menu >>")
    produk = showAllProduct()

    for i,x in enumerate(produk):
        print(f"\nNo.{i + 1}")
        print(f"{x['nama_produk']}")
        print(f"{x['harga']}")
        print(f"Sisa produk : {x['quantity']}")
    
    beli = int(input("Nomor berapa yang pengen anda beli: "))
    jumlah = int(input("Masukan jumlah pembelian: "))
    
    selectedProduct = produk[beli - 1]
    hargaProduk = selectedProduct['harga']
    totalHarga = hargaProduk * jumlah
    idProduk = selectedProduct['IDProduct']
    
    quantityProduk = selectedProduct['quantity']
    if jumlah > quantityProduk:
        print("Barang tidak tersedia")
    else:
        jumlahQ = quantityProduk - jumlah
        kurangQuantity(idProduk, jumlahQ)

    print(f"Anda harus membayar sebesar {totalHarga}")
    
main()