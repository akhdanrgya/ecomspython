import customtkinter
import tkinter.simpledialog
import os
import shutil
from PIL import Image, ImageTk

from libs.productController import *
from libs.kategoriController import *
from libs.transactionController import *

customtkinter.set_appearance_mode("light")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Online Store")
        self.geometry("1500x800")
        self.configure(fg_color="white")
        
        self.protocol("WM_DELETE_WINDOW", self.on_close)
        
        self.content = customtkinter.CTkFrame(self, fg_color="white")
        self.content.pack(side="right", fill="both", expand=True)
        
        self.products = showAllProduct2()
        
        self.displayEcom()
        
    def displayEcom(self):
        header_frame = customtkinter.CTkFrame(self.content, bg_color="#D9D9D9", height=81)
        header_frame.pack(fill="x", padx=10, pady=10)
        header_frame.pack_propagate(False)

        search_entry = customtkinter.CTkEntry(header_frame, font=("ArchivoBlack Regular", 40), bg_color="#FFFFFF", fg_color="#ffffff", placeholder_text="Search", placeholder_text_color="#808080")
        search_entry.pack(side="left", padx=10, fill="x", expand=True)

        kategori_frame = customtkinter.CTkFrame(self.content, bg_color="#CFD7EB")
        kategori_frame.pack(fill="x", padx=10)
        kategori_frame.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)

        kategori_colors = "#406DE0"
        kategori = showAllKategori()
        btn = customtkinter.CTkButton(kategori_frame, text="All", command=self.allProduct, font=("ArchivoBlack Regular", 30), fg_color=kategori_colors, text_color="#FFFFFF")
        btn.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")

        for idx, kat in enumerate(kategori):
            namaKategori = kat["nama_kategori"]
            idKategori = kat["IDKategori"]
            btn = customtkinter.CTkButton(kategori_frame, text=namaKategori, command=lambda id_kat=idKategori: self.filterProductByKategori(id_kat), font=("ArchivoBlack Regular", 30), fg_color=kategori_colors, text_color="#FFFFFF")
            btn.grid(row=0, column=idx + 1, padx=5, pady=10, sticky="nsew")

    def allProduct(self):
        self.displayProducts(self.products)

    def filterProductByKategori(self, idKategori):
        filtered_products = list(filter(lambda x: x['IDKategori'] == idKategori, self.products))
        self.displayProducts(filtered_products)

    def displayProducts(self, products):
        for widget in self.content.winfo_children():
            if isinstance(widget, customtkinter.CTkFrame) and widget not in self.content.winfo_children()[:2]:
                widget.destroy()
        
        content_frame = customtkinter.CTkFrame(self.content, bg_color="#CFD7EB")
        content_frame.pack(fill="both", expand=True, padx=10, pady=10)
        content_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)
        content_frame.grid_rowconfigure((0, 1), weight=1)

        def create_product_frame(parent, row, col, nama, harga, IDProd, idKategori, imgP):
            product_frame = customtkinter.CTkFrame(parent, bg_color="#FFFFFF", corner_radius=10)
            product_frame.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
            
            # Load and display image
            img = Image.open(imgP)
            img = img.resize((150, 150), Image.LANCZOS)
            img = ImageTk.PhotoImage(img)
            img_label = customtkinter.CTkLabel(product_frame, image=img)
            img_label.image = img
            img_label.pack(side="top", padx=10, pady=10)
            
            nama_produk = customtkinter.CTkLabel(product_frame, text=f"{nama}", font=("ArchivoBlack Regular", 24), text_color="#000000", bg_color="#FFFFFF")
            nama_produk.pack(side="bottom", anchor="w", padx=10, pady=10)

            harga_produk = customtkinter.CTkLabel(product_frame, text=f"Rp. {harga}", font=("ArchivoBlack Regular", 15), text_color="#000000", bg_color="#FFFFFF")
            harga_produk.pack(side="bottom", anchor="w", padx=10, pady=(0, 10))

            def buy_action(nama_produk, harga_produk):
                quantity = tkinter.simpledialog.askinteger("Jumlah Pembelian", f"Berapa banyak produk {nama_produk} yang ingin Anda beli?", initialvalue=1)
                if quantity is not None:
                    total_pembayaran = harga_produk * quantity
                    response = tkinter.messagebox.askokcancel("Konfirmasi Pembelian", f"Anda akan membeli {quantity} produk {nama_produk} dengan total pembayaran Rp. {total_pembayaran}. Lanjutkan?")
                    if response:
                        print(f"Anda telah membeli {quantity} produk {nama_produk} dengan total pembayaran Rp. {total_pembayaran}")
                        buy(IDProd, quantity, total_pembayaran, idKategori)
                    else:
                        print("Pembelian dibatalkan")

            btn_beli = customtkinter.CTkButton(product_frame, text="BUY", fg_color="#406DE0", width=20, height=20)
            btn_beli.configure(command=lambda nama=nama, harga=harga: buy_action(nama, harga))
            btn_beli.pack(side="bottom", anchor="e", padx=10, pady=10)

        positions = [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3)]
        for (row, col), prod in zip(positions, products):
            nama = prod['nama_produk']
            harga = prod['harga']
            idprod = prod['IDProduct']
            idKategori = prod['IDKategori']
            img = prod['img']
            create_product_frame(content_frame, row, col, nama, harga, idprod, idKategori, img)

    def on_close(self):
        self.destroy()
        
    def uploadImage(self):
        # Memilih gambar menggunakan file dialog
        file_path = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Image", filetypes=(("Image files", "*.jpg *.jpeg *.png *.gif"), ("All files", "*.*")))
        
        # Mengecek apakah pengguna telah memilih gambar
        if file_path:
            # Menentukan path tujuan untuk menyimpan gambar
            destination_folder = os.path.join(os.getcwd(), "image")
            
            # Mengecek apakah folder image sudah ada, jika tidak, maka akan dibuat
            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)

            # Mengekstrak nama file dari path lengkap
            file_name = os.path.basename(file_path)

            # Menentukan path lengkap untuk file tujuan
            destination_path = os.path.join(destination_folder, file_name)

            # Menyalin gambar ke folder image
            shutil.copy(file_path, destination_path)

            # Mengembalikan path lengkap file yang disalin
            return destination_path

if __name__ == "__main__":
    app = App()
    app.mainloop()
