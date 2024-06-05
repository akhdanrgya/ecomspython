from libs.kategoriController import *
from libs.productController import *
from libs.transactionController import *
from statistik import *
from ecom import App

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
            
        pilih = int(input("Masukan pilihan: "))
        if pilih == 1:
            search = input("Masukan nama produk yang ingin di cari: ")
            searchProduct(search, "nama_produk")
        
        elif pilih == 2:
            search = int(input("Masukan id produk yang ingin di cari: "))
            searchProduct2(search, "IDProduct")
        
        elif pilih == 3:
            search = int(input("Masukan quantity product yang ingin di cari: "))
            searchProduct2(search, "quantity")
        
        elif pilih == 4:
            break
        
        elif pilih == 5:
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
            try:
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
            except Exception as err:
                print(f"Silahkan input dengan benar: {err}")

        elif pilih == 3 :
            try:
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
            
            except Exception as err:
                print(f"Silahkan input dengan benar: {err}")
            
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
            searchProductMenu()

        elif pilih == 6 :
            break
        elif pilih == 7 :
            print("Terimakasih sudah menggunakan aplikasi ini")
            exit()
        else:
            print(f"Menu pilihan {pilih} tidak tersedia.")

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
        
        pilih = int(input("Masukan pilihan: "))

        if pilih == 1:
            search = int(input("Masukan ID transaction yang ingin di cari: "))
            searchTransactions("IDTransaksi", search)
            
        elif pilih == 2:
            search = input("Masukan nama product transaksi yang ingin di cari: ")
            searchTransactions("Nama Product", search)
            
        elif pilih == 3:
            search = int(input("Masukan jumlah transaksi yang ingin di cari: "))
            searchTransactions("Jumlah", search)
            
        elif pilih == 4:
            search = int(input("Masukan total harga transaksi yang ingin di cari: "))
            searchTransactions("Total Harga", search)

        elif pilih == 5:
            break
        
        elif pilih == 6:
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
        
        pilih = int(input("Masukan pilihan: "))

        if pilih == 1:
            transaction = showTransaction()
            
            for i, items in enumerate(transaction):
                print(f"""
                No. {i + 1}
                ID Transaction: {items['IDTransaksi']}
                Nama Product  : {items['Nama Product']}
                Jumlah        : {items['Jumlah']}
                Total Harga   : {items['Total Harga']}
                ID Kategori   : {items['IDKategori']}
                """)
        
        elif pilih == 2 :
            searchTransaction()
        
        elif pilih == 3 :
            break
        
        elif pilih == 4 :
            print("Terimakasih sudah menggunakan aplikasi ini")
            exit()
        else :
            print(f"Menu pilihan {pilih} tidak tersedia")

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
        
        pilih = int(input("Masukan pilihan: "))

        if pilih == 1:
            kategori = showAllKategori()

            for i, items in enumerate(kategori):
                print(f"""
                      No. {i + 1}
                      ID Kategori   : {items['IDKategori']}
                      Nama Kategori : {items['nama_kategori']}
                      """)
        
        elif pilih == 2:
            val = input("Silahkan masukan nama kategori baru: ")

            if not val:
                print("Harus di isi")
            else:
                addKategori(val)
        
        elif pilih == 3:
            try:
                kategori = showAllKategori()

                for i, items in enumerate(kategori):
                    print(f"""
                      No. {i + 1}
                      ID Kategori   : {items['IDKategori']}
                      Nama Kategori : {items['nama_kategori']}
                      """)
                    
                idKategori = int(input("Masukan ID kategori yang ingin di edit: "))

                selectedKategori = None
                for item in kategori:
                    if item['IDKategori'] == idKategori:
                        selectedKategori = item
                        break
                
                if not selectedKategori:
                    print(f"Kategori dengan ID {idKategori} tidak ditemukan!")
                    return
                
                newNama = input("Masukan nama kategori baru (atau kosongkan jika tidak ingin diubah): ") or selectedKategori['nama_kategori']

                updateKategori(idKategori, newNama)
                
            except Exception as err:
                print(f"error: {err}")
        
        elif pilih == 4:
            kategori = showAllKategori()

            for i, items in enumerate(kategori):
                print(f"""
                      No. {i + 1}
                      ID Kategori   : {items['IDKategori']}
                      Nama Kategori : {items['nama_kategori']}
                      """)
            
            dell = int(input("Masukan id kategori yang ingin di hapus: "))

            deleteKategori(dell)
        
        elif pilih == 5:
            while True:
                print("""
                      <<< Search Kategori >>>
                      1. Search kategori By ID
                      2. Search Kategori By Nama Kategori
                      3. Back
                      4. Exit
                      """)
                
                pilih = int(input("Masukan pilihan: "))

                if pilih == 1:
                    val = int(input("Masukan ID Kategori yang ingin di cari: "))

                    searchKategori(val, "IDKategori")
                
                elif pilih == 2:
                    val = input("Masukan nama kategori yang ingin di cari: ")

                    searchKategori(val, "nama_kategori")

                elif pilih == 3:
                    break
                
                elif pilih == 4:
                    print("Terimakasih sudah menggunakan aplikasi ini")
                    exit()
                    
                else:
                    print(f"Pilihan {pilih} tidak tersedia")
        
        elif pilih == 6:
            break
        
        elif pilih == 7:
            print("terimakasih sudah menggunakan aplikasi ini")
            exit()
        
        else:
            print(f"Menu pilihan {pilih} tidak tersedia")

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
        
        pilih = int(input("Masukan pilihan: "))

        if pilih == 1:
            pembelianKategori()
        
        elif pilih == 2:
            plotKategoriTerjual()
        
        elif pilih == 3:
            plotKetersediaanProduk()
        
        elif pilih == 4:
            plotKeuntungan()
        
        elif pilih == 5:
            break
        
        elif pilih == 6:
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
        
        pilih = int(input("Masukan pilihan: "))

        if pilih == 1:
            productMenu()
        elif pilih == 2 :
            dataTransaction()
        elif pilih == 3 :
            kategoriMenu()
        elif pilih == 4 :
            statistikMenu()
        elif pilih == 5 :
            app = App()
            app.mainloop()
            break
        elif pilih == 6 :
            print("Terimakasih sudah menggunakan aplikasi ini")
            exit()
        else:
            print(f"Menu pilihan {pilih} tidak tersedia.")

if __name__ == "__main__":
    main()