import tkinter as tk
from tkinter import ttk
from windows import LoginWindow
from PIL import Image, ImageTk

class Dashboard(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, background="#3B3A4A", width=400)
        self.create_widgets()
        
    def create_widgets(self):
        #Image
        self.image = Image.open("assets/images/logo.png")
        self.image = self.image.resize((80, 70), Image.Resampling.LANCZOS)
        self.image = ImageTk.PhotoImage(self.image)
        #Add Logo
        self.logo = ttk.Label(self, image=self.image, background="#3B3A4A")
        self.logo.pack(pady=10,)

        self.login_button = ttk.Button(self, text="Login", command=self.login)
        self.login_button.pack(pady=10)

    def login(self):
        login_window = LoginWindow(self)