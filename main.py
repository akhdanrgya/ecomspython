"""


KELAS               : SI 23 05
KELOMPOK            : 01
ANGGOTA KELOMPOK    :

Akhdan Anargya Arisadi  (102042300077)
Calista Queena Rumampuk (102042300073)
Ismiati Andini          (102042300056)
Salwa Fadiyah           (102042300052)


"""




from libs.kategoriController import *
from libs.productController import *
from libs.transactionController import *
from statistik import *
from ecom import App

app_0501 = App()

def searchProductMenu():
    while True:
        print("""
            <<< Search Product >>>
            1. Cari Nama Product
            2. Cari ID Product
            3. Cari Quantity Product
            4. Back
            5. Exit
            """)
            
        pilih_0501 = int(input("Masukan pilihan: "))
        if pilih_0501 == 1:
            search = input("Masukan nama produk yang ingin di cari: ")
            searchProduct(search, "nama_produk")
        
        elif pilih_0501 == 2:
            search = int(input("Masukan id produk yang ingin di cari: "))
            searchProduct2(search, "IDProduct")
        
        elif pilih_0501 == 3:
            search = int(input("Masukan quantity product yang ingin di cari: "))
            searchProduct2(search, "quantity")
        
        elif pilih_0501 == 4:
            break
        
        elif pilih_0501 == 5:
            print("Terimakasih sudah menggunakan aplikasi ini")
            exit()

def productMenu():
    while True:
        print("""
              <<< Menu Data Product >>>
              1. Show Data Product 
              2. Add Data Product
              3. Edit Data Product
              4. Delete Data Product
              5. Search Product
              6. Back
              7. Exit
              """)
        
        pilih_0501 = int(input("Masukan Pilihan: "))
        
        if pilih_0501 == 1:
            product_0501 = showAllProduct2()
            
            for i, items_0501 in enumerate(product_0501):
                print(f"""
                No. {i + 1}
                ID Product    : {items_0501['IDProduct']}
                ID Kategori   : {items_0501['IDKategori']}
                Nama Product  : {items_0501['nama_produk']}
                Harga         : {items_0501['harga']}
                Deskripsi     : {items_0501['deskripsi']}
                Gambar        : {items_0501['img']}
                Quantity      : {items_0501['quantity']}
                      """)
                
                
        elif pilih_0501 == 2 :
            try:
                kategori_0501 = showAllKategori()
                for items_0501 in kategori_0501:
                    print(f"Kategori {items_0501['nama_kategori']} dengan angka {items_0501['IDKategori']}")
                inputKategori_0501 = int(input("\nMasukan angka kategori product: "))
                inputNamaProduk_0501 = input("Masukan nama produk: ") 
                inputHargaProduk_0501 = int(input("Masukan harga produk: "))
                inputDeskripsi_0501 = input("Masukan deskripsi produk (optional) : ")

                print("Silahkan pilih gambar untuk produk:")
                inputIMG_0501 = app_0501.uploadImage()

                inputQuantity_0501 = int(input("Masukan jumlah quantity produk: "))
                
                addProduct(inputKategori_0501, inputNamaProduk_0501, inputHargaProduk_0501, inputDeskripsi_0501, inputIMG_0501, inputQuantity_0501)
            except Exception as err:
                print(f"Silahkan input dengan benar: {err}")

        elif pilih_0501 == 3 :
            try:
                product_0501 = showAllProduct2()
                for i, items_0501 in enumerate(product_0501):
                    print(f"""
                    No. {i + 1}
                    ID Product    : {items_0501['IDProduct']}
                    ID Kategori   : {items_0501['IDKategori']}
                    Nama Product  : {items_0501['nama_produk']}
                    Harga         : {items_0501['harga']}
                    Deskripsi     : {items_0501['deskripsi']}
                    Gambar        : {items_0501['img']}
                    Quantity      : {items_0501['quantity']}
                    """)
                
                update_0501 = int(input("Masukan ID product yang akan di update: "))
                selected_product_0501 = None
                for item_0501 in product_0501:
                    if item_0501['IDProduct'] == update_0501:
                        selected_product_0501 = item_0501
                        break
                
                if not selected_product_0501:
                    print(f"Product dengan ID {update_0501} tidak ditemukan!")
                    return

                IDkategori_0501 = input(f"Masukan ID kategori baru (atau kosongkan jika tidak ingin diubah): ") or selected_product_0501['IDKategori']
                nama_0501 = input(f"Masukan nama produk baru (atau kosongkan jika tidak ingin diubah): ") or selected_product_0501['nama_produk']
                harga_0501 = input(f"Masukan harga baru (atau kosongkan jika tidak ingin diubah): ") or selected_product_0501['harga']
                desk_0501 = input(f"Masukan deskripsi baru (atau kosongkan jika tidak ingin diubah): ") or selected_product_0501['deskripsi']
                img_0501 = input(f"Masukan URL gambar baru (atau kosongkan jika tidak ingin diubah): ") or selected_product_0501['img']
                q_0501 = input(f"Masukan quantity baru (atau kosongkan jika tidak ingin diubah): ") or selected_product_0501['quantity']
                
                if harga_0501:
                    harga_0501 = int(harga_0501)
                if q_0501:
                    q_0501 = int(q_0501)


                updateProduct(update_0501, IDkategori_0501, nama_0501, harga_0501, desk_0501, img_0501, q_0501)
            
            except Exception as err:
                print(f"Silahkan input dengan benar: {err}")
            
        elif pilih_0501 == 4 :
            product_0501 = showAllProduct2()
            for i, items_0501 in enumerate(product_0501):
                print(f"""
                No. {i + 1}
                ID Product    : {items_0501['IDProduct']}
                ID Kategori   : {items_0501['IDKategori']}
                Nama Product  : {items_0501['nama_produk']}
                Harga         : {items_0501['harga']}
                Deskripsi     : {items_0501['deskripsi']}
                Gambar        : {items_0501['img']}
                Quantity      : {items_0501['quantity']}
                """)
            
            delete_0501 = int(input("Masukan id produk yang mau di hapus: "))

            deleteProduct(delete_0501)
        
        elif pilih_0501 == 5 :
            searchProductMenu()

        elif pilih_0501 == 6 :
            break
        elif pilih_0501 == 7 :
            print("Terimakasih sudah menggunakan aplikasi ini")
            exit()
        else:
            print(f"Menu pilihan {pilih_0501} tidak tersedia.")

def searchTransaction():
    while True:
        print("""
              <<< Search Data Transaction >>>
              1. Search By ID
              2. Search Product Transaction
              3. Search Jumlah product Transaction
              4. Search Total Harga
              5. Back
              6. Exit
              """)
        
        pilih_0501 = int(input("Masukan pilihan: "))

        if pilih_0501 == 1:
            search = int(input("Masukan ID transaction yang ingin di cari: "))
            searchTransactions("IDTransaksi", search)
            
        elif pilih_0501 == 2:
            search = input("Masukan nama product transaksi yang ingin di cari: ")
            searchTransactions("Nama Product", search)
            
        elif pilih_0501 == 3:
            search = int(input("Masukan jumlah transaksi yang ingin di cari: "))
            searchTransactions("Jumlah", search)
            
        elif pilih_0501 == 4:
            search = int(input("Masukan total harga transaksi yang ingin di cari: "))
            searchTransactions("Total Harga", search)

        elif pilih_0501 == 5:
            break
        
        elif pilih_0501 == 6:
            print("Terimakasih sudah menggunakan aplikasi ini")
            exit()
            
        else:
            print("Pilihan tidak tersedia")

def dataTransaction():
    while True:
        print("""
              <<< Menu Data Transaction >>>
              1. Show Data Transaction
              2. Search Transaction
              3. Back
              4. Exit
              """)
        
        pilih_0501 = int(input("Masukan pilihan: "))

        if pilih_0501 == 1:
            transaction_0501 = showTransaction()
            
            for i, items_0501 in enumerate(transaction_0501):
                print(f"""
                No. {i + 1}
                ID Transaction: {items_0501['IDTransaksi']}
                Nama Product  : {items_0501['Nama Product']}
                Jumlah        : {items_0501['Jumlah']}
                Total Harga   : {items_0501['Total Harga']}
                ID Kategori   : {items_0501['IDKategori']}
                """)
        
        elif pilih_0501 == 2 :
            searchTransaction()
        
        elif pilih_0501 == 3 :
            break
        
        elif pilih_0501 == 4 :
            print("Terimakasih sudah menggunakan aplikasi ini")
            exit()
        else :
            print(f"Menu pilihan {pilih_0501} tidak tersedia")

def kategoriMenu():
    while True:
        print("""
              <<< Menu Data Kategori >>>
              1. Show Data Kategori
              2. Add Data Kategori
              3. Edit Data Kategori
              4. Delete Data Kategori
              5. Search Kategori
              6. Back
              7. Exit
              """)
        
        pilih_0501 = int(input("Masukan pilihan: "))

        if pilih_0501 == 1:
            kategori_0501 = showAllKategori()

            for i, items_0501 in enumerate(kategori_0501):
                print(f"""
                      No. {i + 1}
                      ID Kategori   : {items_0501['IDKategori']}
                      Nama Kategori : {items_0501['nama_kategori']}
                      """)
        
        elif pilih_0501 == 2:
            val_0501 = input("Silahkan masukan nama kategori baru: ")

            if not val_0501:
                print("Harus di isi")
            else:
                addKategori(val_0501)
        
        elif pilih_0501 == 3:
            try:
                kategori_0501 = showAllKategori()

                for i, items_0501 in enumerate(kategori_0501):
                    print(f"""
                      No. {i + 1}
                      ID Kategori   : {items_0501['IDKategori']}
                      Nama Kategori : {items_0501['nama_kategori']}
                      """)
                    
                idKategori_0501 = int(input("Masukan ID kategori yang ingin di edit: "))

                selectedKategori_0501 = None
                for item_0501 in kategori_0501:
                    if item_0501['IDKategori'] == idKategori_0501:
                        selectedKategori_0501 = item_0501
                        break
                
                if not selectedKategori_0501:
                    print(f"Kategori dengan ID {idKategori_0501} tidak ditemukan!")
                    return
                
                newNama_0501 = input("Masukan nama kategori baru (atau kosongkan jika tidak ingin diubah): ") or selectedKategori_0501['nama_kategori']

                updateKategori(idKategori_0501, newNama_0501)
                
            except Exception as err:
                print(f"error: {err}")
        
        elif pilih_0501 == 4:
            kategori_0501 = showAllKategori()

            for i, items_0501 in enumerate(kategori_0501):
                print(f"""
                      No. {i + 1}
                      ID Kategori   : {items_0501['IDKategori']}
                      Nama Kategori : {items_0501['nama_kategori']}
                      """)
            
            dell_0501 = int(input("Masukan id kategori yang ingin di hapus: "))

            deleteKategori(dell_0501)
        
        elif pilih_0501 == 5:
            while True:
                print("""
                      <<< Search Kategori >>>
                      1. Search kategori By ID
                      2. Search Kategori By Nama Kategori
                      3. Back
                      4. Exit
                      """)
                
                pilih_0501 = int(input("Masukan pilihan: "))

                if pilih_0501 == 1:
                    val_0501 = int(input("Masukan ID Kategori yang ingin di cari: "))

                    searchKategori(val_0501, "IDKategori")
                
                elif pilih_0501 == 2:
                    val_0501 = input("Masukan nama kategori yang ingin di cari: ")

                    searchKategori(val_0501, "nama_kategori")

                elif pilih_0501 == 3:
                    break
                
                elif pilih_0501 == 4:
                    print("Terimakasih sudah menggunakan aplikasi ini")
                    exit()
                    
                else:
                    print(f"Pilihan {pilih_0501} tidak tersedia")
        
        elif pilih_0501 == 6:
            break
        
        elif pilih_0501 == 7:
            print("terimakasih sudah menggunakan aplikasi ini")
            exit()
        
        else:
            print(f"Menu pilihan {pilih_0501} tidak tersedia")

def statistikMenu():
    while True:
        print("""
            <<< Menu Statistik >>>
            1. Data Pembelian Berdasarkan Kategori
            2. Data Pembelian Produk Yang Habis Berdasarkan kategori
            3. Data Produk Yang Tersedia
            4. Data Keuntungan Berdasarkan Kategori
            5. Back
            6. Exit
            """)
        
        pilih_0501 = int(input("Masukan pilihan: "))

        if pilih_0501 == 1:
            pembelianKategori()
        
        elif pilih_0501 == 2:
            plotKategoriTerjual()
        
        elif pilih_0501 == 3:
            plotKetersediaanProduk()
        
        elif pilih_0501 == 4:
            plotKeuntungan()
        
        elif pilih_0501 == 5:
            break
        
        elif pilih_0501 == 6:
            print("Terimakasih sudah menggunakan aplikasi ini")
            exit()
    

def main():
    while True:
        print("""
            <<< Menu Toko Online >>>
            1. Data Product
            2. Data Transaction
            3. Data Kategori
            4. Statistik
            5. Ecommerce
            6. Exit
            """)
        
        pilih_0501 = int(input("Masukan pilihan: "))

        if pilih_0501 == 1:
            productMenu()
        elif pilih_0501 == 2 :
            dataTransaction()
        elif pilih_0501 == 3 :
            kategoriMenu()
        elif pilih_0501 == 4 :
            statistikMenu()
        elif pilih_0501 == 5 :
            app_0501.mainloop()
            break
        elif pilih_0501 == 6 :
            print("Terimakasih sudah menggunakan aplikasi ini")
            exit()
        else:
            print(f"Menu pilihan {pilih_0501} tidak tersedia.")

if __name__ == "__main__":
    main()