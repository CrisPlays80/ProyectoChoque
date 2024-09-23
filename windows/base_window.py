import tkinter as tk
from tkinter import ttk

class BaseWindow(tk.Toplevel):
    def __init__(self, parent, title = "Proyecto", width = 400, height = 400):
        super().__init__(parent)
        self.title(title)
        self.geometry(f"{width}x{height}")

        self.header = ttk.Label(self, text=title, style="Header.TLabel")
        self.header.pack(pady = 10)

        self.close_btn = ttk.Button(self, text="X", command=self.destroy)
        self.close_btn.pack(side = "right", pady = 10)