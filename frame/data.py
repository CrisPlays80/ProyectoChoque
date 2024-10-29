from assets.colors.colors import AppStyle
from windows import LoginWindow
from app.connect_db import connect_db

import tkinter as tk
from tkinter import ttk

class Data(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#252330")
        self.create_widgets()
        self.pack(expand=True, fill="both")

    def show_data(self):
        connect = connect_db()
        if connect:
            cursor = connect.cursor()
            cursor.execute("SELECT * FROM DATA_INFO")
            rows = cursor.fetchall()
            self.tree.delete(*self.tree.get_children())
            for row in rows:
                self.tree.insert('', 'end', values=(row[0], row[1]))
            cursor.close()
            connect.close()

    def create_widgets(self):
        self.style = AppStyle()
        self.style.create_label_style("Data.TLabel", font = "Franklin Gothic Medium", background="#252330", foreground="#F5F9F8")

        self.title_label = ttk.Label(self, text="Analytics", style="Data.TLabel")
        self.title_label.place(x=60, y=50)

        self.tree = ttk.Treeview(self, columns=("column1", "column2"), show="headings", height= 20)
        self.tree.heading("column1", text="Velocidad")
        self.tree.heading("column2", text="Orientacion")

        self.tree.column("column1", width=100)
        self.tree.column("column2", width=100)

        self.tree.place(x=40, y=100)

        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.scrollbar.set)
        
        tree_width = self.tree.winfo_reqwidth()  # Obtener el ancho requerido del Treeview
        self.scrollbar.place(x=40 + tree_width, y=100, height=self.tree.winfo_reqheight())

        self.show_data()
        self.update_idletasks()


