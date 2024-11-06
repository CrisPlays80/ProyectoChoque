from assets.colors.colors import AppStyle

from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

from functions.calcular_triage import clasificar_triage

class Dashboard(tk.Frame):
    def __init__(self, parent, content_frame, connect_db, logout_callback, style):
        super().__init__(parent, background="#3B3A4A", width=160)
        self.parent = parent
        self.content_frame = content_frame
        self.connect_db = connect_db
        self.logout_callback = logout_callback
        self.velocidad, self.orientacion, self.triage = [], [], []
        self.style = style
        self.data()
        self.create_widgets()
        self.pack_propagate(False)
        
        self.show_intro_content()

        self.data_indicator = tk.Label(self, text="", background="#3B3A4A")
        self.graph_indicator = tk.Label(self, text="", background="#3B3A4A")
        self.alert_indicator = tk.Label(self, text="", background="#3B3A4A")
        
        self.data_indicator.place(x=27, y=188, width=5, height=26)
        self.graph_indicator.place(x=27, y=317, width=5, height=26)
        self.alert_indicator.place(x=27, y=446 , width=5, height=26)
        
    def create_widgets(self):
        
        # Crear estilos para las etiquetas
        self.style.create_label_style("Dashboard.TLabel")
        
        # Crear estilos para el logo
        self.style.create_label_style("Logo.TLabel", background="#3B3A4A")
        self.style.create_button_style("Dashboard.TButton", borderwidth=0, font_size= 13, background="#353442", tipo = '')

        # Image
        self.image = Image.open("assets/images/logo.png")
        self.image = self.image.resize((95, 95), Image.Resampling.LANCZOS)
        self.image = ImageTk.PhotoImage(self.image)
        
        # Add Logo
        self.logo = ttk.Label(self, image=self.image, style="Logo.TLabel")
        self.logo_padding = ttk.Label(self, text="", background="#3B3A4A")
        self.logo_padding.pack(pady= 60)
        self.logo.place(x = 30, y = 20)

        self.logo.bind("<Button-1>", lambda event: self.show_intro_content())
        
        # Data Button
        self.data_button = ttk.Button(self, text="Datos", style="Dashboard.TButton", command=self.show_data_content)
        self.data_button.pack(pady=50)

        #Graph Button
        self.graph_button = ttk.Button(self, text="Graficos", style="Dashboard.TButton", command=self.show_graph_content)
        self.graph_button.pack(pady=50)

        # Alerts Button
        self.alert_button = ttk.Button(self, text="Alertas", style="Dashboard.TButton", command=self.show_alerts_content)
        self.alert_button.pack(pady=50)
        
        # Line
        self.line = ttk.Separator(self, orient="horizontal")
        self.line.pack(pady=10, fill="x")

        # Logout Button
        self.logout_button = ttk.Button(self, text="Logout", style="Dashboard.TButton", command=self.logout)
        self.logout_button.pack(pady=20)

    def show_intro_content(self):
        from . import Intro
        self.clear_content()
        self.intro = Intro(self.content_frame)

    def show_graph_content(self):
        self.graph_indicator.configure(bg="#5955bc")
        self.data_indicator.configure(bg="#3B3A4A")
        self.alert_indicator.configure(bg="#3B3A4A")
        from . import Graph
        self.clear_content()
        self.graph = Graph(self.content_frame, self.velocidad, self.orientacion, self.triage)

    def show_alerts_content(self):
        self.alert_indicator.configure(bg="#5955bc")
        self.data_indicator.configure(bg="#3B3A4A")
        self.graph_indicator.configure(bg="#3B3A4A")
        from . import AlertTimeline
        self.clear_content()
        self.alerts = AlertTimeline(self.content_frame)

    def show_data_content(self):
        self.alert_indicator.configure(bg="#3B3A4A")
        self.graph_indicator.configure(bg="#3B3A4A")
        self.data_indicator.configure(bg="#5955bc")
        
        from . import Data
        self.clear_content()
        self.data = Data(self.content_frame, self.style, self.velocidad, self.orientacion, self.triage)

    def clear_content(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def logout(self):
        self.logout_callback()

    def data(self):
        if self.connect_db:
            cursor = self.connect_db.cursor()
            cursor.execute("SELECT velocity, orientation FROM DATA_INFO")
            rows = cursor.fetchall()

            for row in rows: #Guardar los datos en listas para el manejo de los datos
                self.velocidad.append(row[0])
                self.orientacion.append(row[1])
                self.triage.append(clasificar_triage(row[0], row[1]))

            cursor.close()