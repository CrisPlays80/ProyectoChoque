import tkinter as tk
from tkinter import ttk


class Header(tk.Frame):
    def __init__(self, parent, connect_db):
        super().__init__(parent, background="#3B3A4A", height=100)
        self.connect_db = connect_db
        self.parent = parent
        self.create_widgets()
        self.pack_propagate(False)

    def create_widgets(self):
        self.label = ttk.Label(self, text=f'Hola, {self.parent.username} bienvenido!',font=("Helvetica", 22), background="#3B3A4A", foreground="#F5F9F8")
        self.label.place(x=30, y=35)


