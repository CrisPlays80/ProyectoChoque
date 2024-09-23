import tkinter as tk
from tkinter import ttk

class Header(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_widgets()
        
    def create_widgets(self):
        self.title_label = ttk.Label(self, text="My Application")
        self.title_label.pack()