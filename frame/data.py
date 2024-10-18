from assets.colors.colors import AppStyle

import tkinter as tk
from tkinter import ttk

class Data(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#252330")
        self.configure(bg="#FFFFFF")
        self.create_widgets()
        self.pack()

    def create_widgets(self):
        self.style = AppStyle()

        self.title_label = ttk.Label(self, text="Datos", style="Data.TLabel")
        self.title_label.pack(pady=60)
