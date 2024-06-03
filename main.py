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
        
        self.sidebar = customtkinter.CTkFrame(self, width=200, fg_color="#20232A", bg_color="#20232A")
        self.sidebar.pack(side="left", fill="y")
        
        self.content = customtkinter.CTkFrame(self, fg_color="white")
        self.content.pack(side="right", fill="both", expand=True)
        
        self.sideBar()
        self.display_home()
    
    def sideBar(self):
        label = customtkinter.CTkLabel(self.sidebar, text="Online Store Management", font=("Arial", 24), text_color="white")
        label.pack(pady=10)
        
        buttons = [
            ("Home", self.display_home),
            ("Insert Data", self.display_insert_data),
            ("Edit Data", self.display_edit_data),
            ("Delete Data", self.display_delete_data),
            ("Search", self.display_search_data),
            ("Data Transaksi", self.display_transaction),
            ("E-Commerce", self.displayEcom)
        ]
        
        for (text, command) in buttons:
            button = customtkinter.CTkButton(self.sidebar, text=text, font=("Arial", 18), width=200, height=50, command=command)
            button.pack(fill="x", pady=10)
    
    def clear_content(self):
        for widget in self.content.winfo_children():
            widget.destroy()
    
    def display_home(self):
        self.clear_content()
        label = customtkinter.CTkLabel(self.content, text="Welcome to the Online Store Management System", font=("Arial", 24))
        label.pack(pady=20)

        product = showAllProduct2()

        if not product:
            customtkinter.CTkLabel(self.content, text="Tidak Ada Product", font=("Arial", 24)).pack(pady=20)
        else:
            style = ttk.Style()
            style.configure("Treeview", 
                            background="white", 
                            foreground="black", 
                            rowheight=25, 
                            fieldbackground="white")
            style.configure("Treeview.Heading", font=('Arial', 12, 'bold'))
            view = ttk.Treeview(self.content, columns=("No", "IDKategori", "nama_produk", "harga", "deskripsi", "quantity"), show="headings")
            view.heading("No", text="No")
            view.heading("IDKategori", text="IDKategori")
            view.heading("nama_produk", text="Nama Produk")
            view.heading("harga", text="Harga")
            view.heading("deskripsi", text="Deskripsi")
            view.heading("quantity", text="Quantity")
            view.column("No", width=100)
            view.column("IDKategori", width=100)
            view.column("nama_produk", width=150)
            view.column("harga", width=100)
            view.column("deskripsi", width=250)
            view.column("quantity", width=100)

            for no, items in enumerate(product):
                view.insert("", "end", values= (no + 1, items['IDKategori'], items['nama_produk'], items['harga'], items['deskripsi'], items['quantity']))
            
            view.pack(padx=20, pady=20, fill="both", expand=True)

    def display_transaction(self):
        self.clear_content()
        label = customtkinter.CTkLabel(self.content, text="Data Transaksi", font=("Arial", 24))
        label.pack(pady=20)
        
        transaksi = showTransaction()

        if not transaksi:
            customtkinter.CTkLabel(self.content, text="Tidak Ada Transaksi", font=("Arial", 24)).pack(pady=20)
        else:
            style = ttk.Style()
            style.configure("Treeview", 
                            background="white", 
                            foreground="black", 
                            rowheight=25, 
                            fieldbackground="white")
            style.configure("Treeview.Heading", font=('Arial', 12, 'bold'))
            view = ttk.Treeview(self.content, columns=("No","Nama Product", "Jumlah", "Total Harga"), show="headings")
            view.heading("No", text="No")
            view.heading("Nama Product", text="Nama Product")
            view.heading("Jumlah", text="Jumlah")
            view.heading("Total Harga", text="Total Harga")

            view.column("No", width=5)
            view.column("Nama Product", width=100)
            view.column("Jumlah", width=100)
            view.column("Total Harga", width=150)

            for no, data in enumerate(transaksi):
                view.insert("", "end", values=(no + 1 ,data['Nama Product'], data['Jumlah'], data['Total Harga']))

            view.pack(padx=20, pady=20, fill="both", expand=True)


    def display_insert_data(self):
        self.clear_content()
        
        def add_product():
            idkategori = entry_idkategori.get()
            nama = entry_nama.get()
            harga = entry_harga.get()
            desc = entry_desc.get()
            img = entry_img.get()
            quantity = entry_quantity.get()

            addProduct(idkategori, nama, harga, desc, img, quantity)

        label = customtkinter.CTkLabel(self.content, text="Insert Product Data", font=("Arial", 24))
        label.pack(pady=20)
        
        form_frame = customtkinter.CTkFrame(self.content)
        form_frame.pack(pady=20)

        labels = ["ID Kategori:", "Nama Produk:", "Harga:", "Deskripsi:", "Gambar URL:", "Quantity:"]
        entries = []

        for i, label_text in enumerate(labels):
            label = customtkinter.CTkLabel(form_frame, text=label_text, font=("Arial", 18))
            label.grid(row=i, column=0, padx=10, pady=10)
            entry = customtkinter.CTkEntry(form_frame)
            entry.grid(row=i, column=1, padx=10, pady=10)
            entries.append(entry)

        entry_idkategori, entry_nama, entry_harga, entry_desc, entry_img, entry_quantity = entries
        
        add_button = customtkinter.CTkButton(form_frame, text="Add Product", command=add_product)
        add_button.grid(row=6, column=0, columnspan=2, pady=20)
        
        output_text = customtkinter.CTkTextbox(self.content, height=10)
        output_text.pack(pady=20, padx=20, fill="both", expand=True)
        
    def display_edit_data(self):
        self.clear_content()
        
        label = customtkinter.CTkLabel(self.content, text="Edit Product Data", font=("Arial", 24))
        label.pack(pady=20)

        fields = ["ID Product", "ID Kategori", "Nama Produk", "Harga", "Deskripsi", "Image URL", "Quantity"]
        entries = {}

        for field in fields:
            frame = customtkinter.CTkFrame(self.content)
            frame.pack(pady=5, padx=10, fill="x")

            label = customtkinter.CTkLabel(frame, text=field, font=("Arial", 12))
            label.pack(side="left", padx=10)

            entry = customtkinter.CTkEntry(frame, font=("Arial", 12))
            entry.pack(side="right", fill="x", expand=True, padx=10)
            entries[field] = entry

        def on_submit():
            id = entries["ID Product"].get()
            IDkategori = entries["ID Kategori"].get()
            nama = entries["Nama Produk"].get()
            harga = entries["Harga"].get()
            desk = entries["Deskripsi"].get()
            img = entries["Image URL"].get()
            q = entries["Quantity"].get()

            updateProduct(id, IDkategori, nama, harga, desk, img, q)

        submit_button = customtkinter.CTkButton(self.content, text="Update", command=on_submit)
        submit_button.pack(pady=20)
        
    def display_delete_data(self):
        self.clear_content()
        label = customtkinter.CTkLabel(self.content, text="Delete Product Data", font=("Arial", 24))
        label.pack(pady=20)

    def display_search_data(self):
        self.clear_content()
        label = customtkinter.CTkLabel(self.content, text="Search Product Data", font=("Arial", 24))
        label.pack(pady=20)
    
    
    def displayEcom(self):
        self.clear_content()
        
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
            btn_beli.configure(command=lambda nama=nama, harga=harga: buy_action(nama, harga))  # Menyertakan argumen nama_produk dan harga_produk ke dalam fungsi buy_action
            btn_beli.pack(side="bottom", anchor="e", padx=10, pady=10)

        products = showAllProduct2()

        positions = [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3)]
        for (row, col), prod in zip(positions, products):
            nama = prod['nama_produk']
            harga = prod['harga']
            idprod = prod['IDProduct']
            create_product_frame(content_frame, row, col, nama, harga, idprod)


if __name__ == "__main__":
    app = App()
    app.mainloop()
