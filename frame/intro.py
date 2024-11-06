import tkinter as tk
from tkinter import ttk

class Intro(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg = "#252330")
        self.create_widgets()
        self.pack(expand=True, fill="both")

    def create_widgets(self):
        self.title = tk.Label(
            self,
            text="TriageCare",
            font=("CreatoDisplay-Bold", 20),
            background="#252330",
            foreground="#F5F9F8",
        )
        self.title.pack(pady=10)

        self.description = tk.Label(
            self,
            text="""Nuestro proyecto esta encaminado a dar una rapida respuesta ante
accidentes de transito a traves de una mejora a los sistemas de 
alertamiento a los cuerpos de emergencia mas cercanos, usando redes
satelitales evitaremos el problema de no poder alertar si en la zona del 
accidente no hay cobertura de señal de internet, ademas de tener un 
sistema de consulta donde las personas pueden acceder y consultar los 
accidentes mas recientes con sus caracteristicas como velocidad y
orientacion de choque, asi como la clasificacion del triaje que se le da a los
pacientes involucrados en el accidente. Tambien podran acceder a
diferentes graficas con informacion relevante sobre estos accidentes para
una mejor comprension al usuario.""",
            font=("CreatoDisplay-Regular", 12),
            background="#252330",
            foreground="#F5F9F8",
            justify="left",
            anchor="center",
        )
        self.description.pack(pady=10)