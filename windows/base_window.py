import tkinter as tk
from tkinter import ttk

class BaseWindow(tk.Toplevel):
    def __init__(self, parent, title = "Proyecto", width = 400, height = 400):
        super().__init__(parent)
        self.title(title)
        self.geometry(f"{width}x{height}")

        wtotal = self.winfo_screenwidth()
        htotal = self.winfo_screenheight()

        wventana = width
        hventana = height
        #  Aplicamos la siguiente formula para calcular donde debería posicionarse
        pwidth = round(wtotal/2-wventana/2)
        pheight = round(htotal/2-hventana/2)
        #  Se lo aplicamos a la geometría de la ventana
        self.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight))