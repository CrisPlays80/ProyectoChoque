import tkinter as tk
from tkinter import ttk

class Header(tk.Frame):
    def __init__(self, parent, connect_db, style):
        super().__init__(parent, background="#3B3A4A", height=120)
        self.connect_db = connect_db
        self.parent = parent
        self.style = style
        self.create_widgets()
        self.pack_propagate(False)

    def create_widgets(self):

        # Crear estilos para las etiquetas
        self.style.create_label_style("Header.TLabel", font_size=22, background="#3B3A4A", foreground="#F5F9F8")

        self.label = ttk.Label(self, text=f'Hola, {self.parent.username}!', style="Header.TLabel")
        self.label.place(x=30, y=45)


