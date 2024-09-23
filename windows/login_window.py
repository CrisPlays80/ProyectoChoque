from .base_window import BaseWindow
import tkinter as tk
from tkinter import ttk

class LoginWindow(BaseWindow):
    def __init__(self, parent):
        super().__init__(parent, title = "Login", width = 400, height = 400)

        self.username_label = ttk.Label(self, text="Username:")
        self.username_label.pack(pady=5)
        self.username_entry = ttk.Entry(self)
        self.username_entry.pack(pady=5)

        self.password_label = ttk.Label(self, text="Password:")
        self.password_label.pack(pady=5)
        self.password_entry = ttk.Entry(self, show="*")
        self.password_entry.pack(pady=5)

        # Login button
        self.login_button = ttk.Button(self, text="Login", command=self.login)
        self.login_button.pack(pady=20)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        print(f"Logging in with {username}/{password}")