import tkinter as tk
from tkinter import ttk

from assets.colors.colors import AppStyle

class Header(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, background="#3B3A4A", height=100)
        self.create_widgets()
        self.pack_propagate(False)

    def create_widgets(self):
        self.label = ttk.Label(self, text="Header", background="#3B3A4A", foreground="#F5F9F8")
        self.label.pack(side="right", padx=10)