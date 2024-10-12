from assets.colors.colors import AppStyle

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class Dashboard(tk.Frame):
    def __init__(self, parent, content_frame):
        super().__init__(parent, background="#3B3A4A", width=160)
        self.content_frame = content_frame
        self.create_widgets()
        
    def create_widgets(self):
        self.style = AppStyle()
        
        # Crear estilos para las etiquetas
        self.style.create_label_style("Dashboard.TLabel", font="Helvetica", font_size=15, background="#3B3A4A", foreground="#F5F9F8")
        
        # Crear estilos para el logo
        self.style.create_label_style("Logo.TLabel", font="Helvetica", font_size=15, background="#3B3A4A", foreground="#FFFFFF")
        
        # Image
        self.image = Image.open("assets/images/logo.png")
        self.image = self.image.resize((100, 90), Image.Resampling.LANCZOS)
        self.image = ImageTk.PhotoImage(self.image)
        
        # Add Logo
        self.logo = ttk.Label(self, image=self.image, style="Logo.TLabel")
        self.logo.pack(pady=10)
        
        # Data Label
        self.data_label = ttk.Label(self, text="Datos", style="Dashboard.TLabel")
        self.data_label.pack(pady=60)
        self.data_label.bind("<Button-1>", self.show_data_content)

        # Alerts Label
        self.alert_label = ttk.Label(self, text="Alertas", style="Dashboard.TLabel")
        self.alert_label.pack(pady=50)
        
        # Line
        self.line = ttk.Separator(self, orient="horizontal")
        self.line.pack(pady=10, fill="x")

        self.pack_propagate(False)

    def show_data_content(self,event):
        print("HELLO WORLD")
        self.clear_content()
        ttk.Label(self.content_frame, text="Content", style="Dashboard.TLabel").pack(pady=60)

    def clear_content(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()