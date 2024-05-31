import customtkinter
from tkinter import ttk
import matplotlib.pyplot as plt
from libs.productController import *
from libs.kategoriController import *

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
            ("Search", self.display_search_data)
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

            product = showAllProduct()

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
                
                view = ttk.Treeview(self.content, columns=("IDProduct", "IDKategori", "nama_produk", "harga", "deskripsi", "quantity"), show="headings")
                view.heading("IDProduct", text="IDProduct")
                view.heading("IDKategori", text="IDKategori")
                view.heading("nama_produk", text="Nama Produk")
                view.heading("harga", text="Harga")
                view.heading("deskripsi", text="Deskripsi")
                view.heading("quantity", text="Quantity")
                view.column("IDProduct", width=100)
                view.column("IDKategori", width=100)
                view.column("nama_produk", width=150)
                view.column("harga", width=100)
                view.column("deskripsi", width=250)
                view.column("quantity", width=100)

                for items in product:
                    view.insert("", "end", values=items)
                
                view.pack(fill="both", expand=True, pady=10)

    
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

        # Form fields
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

if __name__ == "__main__":
    app = App()
    app.mainloop()