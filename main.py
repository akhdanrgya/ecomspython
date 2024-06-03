import customtkinter
from tkinter import ttk
import tkinter.simpledialog

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
        
        self.displayEcom()
        
    def displayEcom(self):
        header_frame = customtkinter.CTkFrame(self.content, bg_color="#D9D9D9", height=81)
        header_frame.pack(fill="x", padx=10, pady=10)
        header_frame.pack_propagate(False)

        search_entry = customtkinter.CTkEntry(header_frame, font=("ArchivoBlack Regular", 40), bg_color="#FFFFFF", fg_color="#ffffff", placeholder_text="Search", placeholder_text_color="#808080")
        search_entry.pack(side="left", padx=10, fill="x", expand = True)

        kategori_frame = customtkinter.CTkFrame(self.content, bg_color="#CFD7EB")
        kategori_frame.pack(fill="x", padx=10)
        kategori_frame.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)

        kategori_colors = "#406DE0"
        kategori = showAllKategori()

        for idx,kat in enumerate(kategori):
            namaKategori = kat["nama_kategori"]
            btn = customtkinter.CTkButton(kategori_frame, text=namaKategori, font=("ArchivoBlack Regular", 30), fg_color=kategori_colors, text_color="#FFFFFF")
            btn.grid(row=0, column=idx, padx=5, pady=10, sticky="nsew")

        content_frame = customtkinter.CTkFrame(self.content, bg_color="#CFD7EB")
        content_frame.pack(fill="both", expand=True, padx=10, pady=10)
        content_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)
        content_frame.grid_rowconfigure((0, 1), weight=1)

        def create_product_frame(parent, row, col, nama, harga, IDProd):
            product_frame = customtkinter.CTkFrame(parent, bg_color="#FFFFFF", corner_radius=10)
            product_frame.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
            
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
                        buy(IDProd, quantity, total_pembayaran)
                    else:
                        print("Pembelian dibatalkan")

            btn_beli = customtkinter.CTkButton(product_frame, text="BUY", fg_color="#406DE0", width=20, height=20)
            btn_beli.configure(command=lambda nama=nama, harga=harga: buy_action(nama, harga))
            btn_beli.pack(side="bottom", anchor="e", padx=10, pady=10)

        products = showAllProduct2()

        positions = [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3)]
        for (row, col), prod in zip(positions, products):
            nama = prod['nama_produk']
            harga = prod['harga']
            idprod = prod['IDProduct']
            create_product_frame(content_frame, row, col, nama, harga, idprod)
    
    def on_close(self):
        self.destroy()

if __name__ == "__main__":
    app = App()
    app.mainloop()
