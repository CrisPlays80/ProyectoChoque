from assets.colors.colors import AppStyle

from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class Dashboard(tk.Frame):
    def __init__(self, parent, content_frame, connect_db):
        super().__init__(parent, background="#3B3A4A", width=160)
        self.content_frame = content_frame
        self.connect_db = connect_db
        self.create_widgets()
        self.pack_propagate(False)
        
    def create_widgets(self):
        self.style = AppStyle()
        
        # Crear estilos para las etiquetas
        self.style.create_label_style("Dashboard.TLabel", font="Helvetica", font_size=15, background="#3B3A4A", foreground="#F5F9F8")
        
        # Crear estilos para el logo
        self.style.create_label_style("Logo.TLabel", font="Helvetica", font_size=15, background="#3B3A4A", foreground="#FFFFFF")
        self.style.create_button_style("Dashboard.TButton", font="Helvetica", font_size=15, background="#3B3A4A", foreground="#F5F9F8", borderwidth=0)

        # Image
        self.image = Image.open("assets/images/logo.png")
        self.image = self.image.resize((100, 90), Image.Resampling.LANCZOS)
        self.image = ImageTk.PhotoImage(self.image)
        
        # Add Logo
        self.logo = ttk.Label(self, image=self.image, style="Logo.TLabel")
        self.logo.pack(pady=10)
        
        # Data Button
        self.data_button = ttk.Button(self, text="Datos", style="Dashboard.TButton", command=self.show_data_content)
        self.data_button.pack(pady=60)

        # Alerts Button
        self.alert_button = ttk.Button(self, text="Alertas", style="Dashboard.TButton", command=self.show_alerts_content)
        self.alert_button.pack(pady=50)
        
        # Line
        self.line = ttk.Separator(self, orient="horizontal")
        self.line.pack(pady=10, fill="x")

    def show_alerts_content(self):
        """ from . import Alerts
        self.clear_content()
        self.alerts = Alerts(self.content_frame) """
        messagebox.showinfo("Alertas", "En proceso mi profe.....")

    def show_data_content(self):
        from . import Data
        self.clear_content()
        self.data = Data(self.content_frame, self.connect_db)

    def clear_content(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()