import tkinter as tk
from tkinter import ttk

from assets.colors.colors import AppStyle

class Header(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, background="#3B3A4A")
        self.create_widgets()

    def create_widgets(self):
        self.style = AppStyle()
        