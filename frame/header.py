from assets.colors.colors import AppStyle
from windows import LoginWindow

import tkinter as tk
from tkinter import ttk


class Header(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, background="#3B3A4A", height=100)
        self.create_widgets()
        self.pack_propagate(False)

    def create_widgets(self):
        self.label = ttk.Label(self, text="Header", background="#3B3A4A", foreground="#F5F9F8")
        self.label.pack(side="right", padx=10)

        self.login_button = ttk.Button(self, text="Login", command=self.login)
        self.login_button.pack(side="right", padx=10)
    
    def login(self):
        self.login_window = LoginWindow(self)