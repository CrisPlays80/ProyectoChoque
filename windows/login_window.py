from .base_window import BaseWindow
import tkinter as tk
from tkinter import ttk
from assets.colors.colors import AppStyle

class LoginWindow(BaseWindow):
    def __init__(self, parent):
        super().__init__(parent, title="Login", width=400, height=250)
        self.configure(bg="#575669")
        self.resizable(False, False)

        # Crear una instancia de AppStyle y definir estilos únicos
        self.style = AppStyle()
        self.style.create_label_style("LoginWindow.TLabel", font="Helvetica", background="#575669", foreground="white")
        self.style.create_button_style("LoginWindow.TButton", font="Helvetica", background="#3B3A4A", foreground="white")
    
        # Username Label
        self.username_label = ttk.Label(self, text="Username:", style="LoginWindow.TLabel")
        self.username_label.pack(pady=20)

        # Username Entry
        self.username_entry = ttk.Entry(self)
        self.username_entry.pack(pady=0)

        # Password Label
        self.password_label = ttk.Label(self, text="Password:", style="LoginWindow.TLabel")
        self.password_label.pack(pady=20)

        # Password Entry
        self.password_entry = ttk.Entry(self, show="*")
        self.password_entry.pack(pady=0)

        # Login Button
        self.login_button = ttk.Button(self, text="Login", command=self.login, style="LoginWindow.TButton")
        self.login_button.pack(pady=30)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        print(f"Logging in with {username}/{password}")
