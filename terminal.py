from libs.kategoriController import *
from libs.productController import *
from libs.transactionController import *
import matplotlib as plt

def productMenu():
    while True:
        print("""
              <<< Menu Data Product >>>
              1. Show Data Product 
              2. Add Data Product
              3. Edit Data Product
              4. Delete Data Product
              5. Back
              6. Exit
              """)
        
        pilih = int(input("Masukan Pilihan: "))
        
        if pilih == 1:
            product = showAllProduct2()
            
            for i, items in enumerate(product):
                print(f"""
                No. {i + 1}
                ID Product    : {items['IDProduct']}
                ID Kategori   : {items['IDKategori']}
                Nama Product  : {items['nama_produk']}
                Harga         : {items['harga']}
                Deskripsi     : {items['deskripsi']}
                Gambar        : {items['img']}
                Quantity      : {items['quantity']}
                      """)
                
                
        elif pilih == 2 :
            kategori = showAllKategori()
            for items in kategori:
                print(f"Kategori {items['nama_kategori']} dengan angka {items['IDKategori']}")
            inputKategori = int(input("\nMasukan angka kategori product: "))
            inputNamaProduk = input("Masukan nama produk: ") 
            inputHargaProduk = int(input("Masukan harga produk: "))
            inputDeskripsi = input("Masukan deskripsi produk (optional) : ")
            inputIMG = input("Masukan url gambar produk: ")
            inputQuantity = int(input("Masukan jumlah quantity produk: "))
            
            addProduct(inputKategori, inputNamaProduk, inputHargaProduk, inputDeskripsi, inputIMG, inputQuantity)
            
        elif pilih == 3 :
            product = showAllProduct2()
            for i, items in enumerate(product):
                print(f"""
                No. {i + 1}
                ID Product    : {items['IDProduct']}
                ID Kategori   : {items['IDKategori']}
                Nama Product  : {items['nama_produk']}
                Harga         : {items['harga']}
                Deskripsi     : {items['deskripsi']}
                Gambar        : {items['img']}
                Quantity      : {items['quantity']}
                """)
            
            update = int(input("Masukan ID product yang akan di update: "))


            selected_product = None
            for item in product:
                if item['IDProduct'] == update:
                    selected_product = item
                    break
            
            if not selected_product:
                print(f"Product dengan ID {update} tidak ditemukan!")
                return

            # Input fields to update, use current values if input is empty
            IDkategori = input(f"Masukan ID kategori baru (atau kosongkan jika tidak ingin diubah): ") or selected_product['IDKategori']
            nama = input(f"Masukan nama produk baru (atau kosongkan jika tidak ingin diubah): ") or selected_product['nama_produk']
            harga = input(f"Masukan harga baru (atau kosongkan jika tidak ingin diubah): ") or selected_product['harga']
            desk = input(f"Masukan deskripsi baru (atau kosongkan jika tidak ingin diubah): ") or selected_product['deskripsi']
            img = input(f"Masukan URL gambar baru (atau kosongkan jika tidak ingin diubah): ") or selected_product['img']
            q = input(f"Masukan quantity baru (atau kosongkan jika tidak ingin diubah): ") or selected_product['quantity']
            
            if harga:
                harga = int(harga)
            if q:
                q = int(q)
            

            updateProduct(update, IDkategori, nama, harga, desk, img, q)
   
        elif pilih == 4 :
            product = showAllProduct2()
            for i, items in enumerate(product):
                print(f"""
                No. {i + 1}
                ID Product    : {items['IDProduct']}
                ID Kategori   : {items['IDKategori']}
                Nama Product  : {items['nama_produk']}
                Harga         : {items['harga']}
                Deskripsi     : {items['deskripsi']}
                Gambar        : {items['img']}
                Quantity      : {items['quantity']}
                """)
            
            delete = int(input("Masukan id produk yang mau di hapus: "))

            deleteProduct(delete)
            
        elif pilih == 5 :
            break
        elif pilih == 6 :
            print("Terimakasih sudah menggunakan aplikasi ini")
            exit()
        else:
            print(f"Menu pilihan {pilih} tidak tersedia.")

def main():
    while True:
        print("""
            <<< Menu Toko Online >>>
            1. Data Product
            2. Data Transaction
            3. Data Kategori
            4. Statistik
            5. Exit
            """)
        
        pilih = int(input("Masukan pilihan: "))

        if pilih == 1:
            productMenu()
        elif pilih == 2 :
            print("2")
        elif pilih == 3 :
            print("2")
        elif pilih == 4 :
            print("4")
        elif pilih == 5 :
            print("Terimakasih sudah menggunakan aplikasi ini")
            exit()
        else:
            print(f"Menu pilihan {pilih} tidak tersedia.")

if __name__ == "__main__":
    main()