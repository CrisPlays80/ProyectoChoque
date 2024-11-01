from windows import LoginWindow

import tkinter as tk
from tkinter import ttk


class Header(tk.Frame):
    def __init__(self, parent, connect_db):
        super().__init__(parent, background="#3B3A4A", height=100)
        self.connect_db = connect_db
        self.create_widgets()
        self.pack_propagate(False)

    def create_widgets(self):
        self.label = ttk.Label(self, font=("Helvetica", 22), background="#3B3A4A", foreground="#F5F9F8")
        self.label.place(x=30, y=35)

        self.login_button = ttk.Button(self, text="Login", command=self.login)
        self.login_button.pack(side="right", padx=10)
    
    def username(self, username):
        self.label.config(text=f'Hola, {username} bienvenido!')
        self.login_button.destroy()

    def login(self):
        self.login_window = LoginWindow(self, self.connect_db, self.username)