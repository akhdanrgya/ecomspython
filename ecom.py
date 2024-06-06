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
        
        self.content_0501 = customtkinter.CTkFrame(self, fg_color="white")
        self.content_0501.pack(side="right", fill="both", expand=True)
        
        self.products_0501 = showAllProduct2()
        
        self.displayEcom()
        
    def displayEcom(self):
        header_frame_0501 = customtkinter.CTkFrame(self.content_0501, bg_color="#D9D9D9", height=81)
        header_frame_0501.pack(fill="x", padx=10, pady=10)
        header_frame_0501.pack_propagate(False)

        kategori_frame_0501 = customtkinter.CTkFrame(self.content_0501, bg_color="#CFD7EB")
        kategori_frame_0501.pack(fill="x", padx=10)
        kategori_frame_0501.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)

        kategori_colors_0501 = "#406DE0"
        kategori_0501 = showAllKategori()
        btn_0501 = customtkinter.CTkButton(kategori_frame_0501, text="All", command=self.allProduct, font=("ArchivoBlack Regular", 30), fg_color=kategori_colors_0501, text_color="#FFFFFF")
        btn_0501.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")

        for idx, kat_0501 in enumerate(kategori_0501):
            namaKategori_0501 = kat_0501["nama_kategori"]
            idKategori_0501 = kat_0501["IDKategori"]
            btn_0501 = customtkinter.CTkButton(kategori_frame_0501, text=namaKategori_0501, command=lambda id_kat=idKategori_0501: self.filterProductByKategori(id_kat), font=("ArchivoBlack Regular", 30), fg_color=kategori_colors_0501, text_color="#FFFFFF")
            btn_0501.grid(row=0, column=idx + 1, padx=5, pady=10, sticky="nsew")

    def allProduct(self):
        self.displayProducts(self.products_0501)

    def filterProductByKategori(self, idKategori):
        filtered_products_0501 = list(filter(lambda x: x['IDKategori'] == idKategori, self.products_0501))
        self.displayProducts(filtered_products_0501)

    def displayProducts(self, products_0501):
        for widget_0501 in self.content_0501.winfo_children():
            if isinstance(widget_0501, customtkinter.CTkFrame) and widget_0501 not in self.content_0501.winfo_children()[:2]:
                widget_0501.destroy()
        
        content_frame_0501 = customtkinter.CTkFrame(self.content_0501, bg_color="#CFD7EB")
        content_frame_0501.pack(fill="both", expand=True, padx=10, pady=10)
        content_frame_0501.grid_columnconfigure((0, 1, 2, 3), weight=1)
        content_frame_0501.grid_rowconfigure((0, 1), weight=1)

        def create_product_frame(parent_0501, row_0501, col_0501, nama_0501, harga_0501, IDProd_0501, idKategori_0501, imgP_0501):
            product_frame_0501 = customtkinter.CTkFrame(parent_0501, bg_color="#FFFFFF", corner_radius=10)
            product_frame_0501.grid(row=row_0501, column=col_0501, padx=5, pady=5, sticky="nsew")
            
            img_0501 = Image.open(imgP_0501)
            img_0501 = img_0501.resize((300, 300), Image.LANCZOS)
            img_0501 = ImageTk.PhotoImage(img_0501)
            
            img_label_0501 = customtkinter.CTkLabel(product_frame_0501, image=img_0501, text="")
            img_label_0501.image = img_0501
            img_label_0501.pack(expand = True)
            
            nama_produk_0501 = customtkinter.CTkLabel(product_frame_0501, text=f"{nama_0501}", font=("ArchivoBlack Regular", 24), text_color="#000000", bg_color="#FFFFFF")
            nama_produk_0501.pack(side="bottom", anchor="w", padx=10, pady=10)

            harga_produk_0501 = customtkinter.CTkLabel(product_frame_0501, text=f"Rp. {harga_0501}", font=("ArchivoBlack Regular", 15), text_color="#000000", bg_color="#FFFFFF")
            harga_produk_0501.pack(side="bottom", anchor="w", padx=10, pady=(0, 10))

            def buy_action(nama_produk_0501, harga_produk):
                quantity_0501 = tkinter.simpledialog.askinteger("Jumlah Pembelian", f"Berapa banyak produk {nama_produk_0501} yang ingin Anda beli?", initialvalue=1)
                if quantity_0501 is not None:
                    total_pembayaran_0501 = harga_produk * quantity_0501
                    response_0501 = tkinter.messagebox.askokcancel("Konfirmasi Pembelian", f"Anda akan membeli {quantity_0501} produk {nama_produk_0501} dengan total pembayaran Rp. {total_pembayaran_0501}. Lanjutkan?")
                    if response_0501:
                        print(f"Anda telah membeli {quantity_0501} produk {nama_produk_0501} dengan total pembayaran Rp. {total_pembayaran_0501}")
                        buy(IDProd_0501, quantity_0501, total_pembayaran_0501, idKategori_0501)
                    else:
                        print("Pembelian dibatalkan")

            btn_beli_0501 = customtkinter.CTkButton(product_frame_0501, text="BUY", fg_color="#406DE0", width=20, height=20)
            btn_beli_0501.configure(command=lambda nama=nama_0501, harga=harga_0501: buy_action(nama, harga))
            btn_beli_0501.pack(side="bottom", anchor="e", padx=10, pady=10)

        positions_0501 = [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3)]
        for (row, col), prod_0501 in zip(positions_0501, products_0501):
            nama_0501 = prod_0501['nama_produk']
            harga_0501 = prod_0501['harga']
            idprod_0501 = prod_0501['IDProduct']
            idKategori_0501 = prod_0501['IDKategori']
            img_0501 = prod_0501['img']
            create_product_frame(content_frame_0501, row, col, nama_0501, harga_0501, idprod_0501, idKategori_0501, img_0501)

    def on_close(self):
        self.destroy()
        
    def uploadImage(self):
        file_path_0501 = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Image", filetypes=(("Image files", "*.jpg *.jpeg *.png *.gif"), ("All files", "*.*")))
        
        if file_path_0501:
            destination_folder_0501 = os.path.join(os.getcwd(), "image")
            
            if not os.path.exists(destination_folder_0501):
                os.makedirs(destination_folder_0501)

            file_name_0501 = os.path.basename(file_path_0501)

            destination_path_0501 = os.path.join(destination_folder_0501, file_name_0501)
            shutil.copy(file_path_0501, destination_path_0501)
            return destination_path_0501

if __name__ == "__main__":
    app_0501 = App()
    app_0501.mainloop()
