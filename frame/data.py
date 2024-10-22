from assets.colors.colors import AppStyle
from windows import LoginWindow

import tkinter as tk
from tkinter import ttk

class Data(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#252330")
        self.create_widgets()
        self.pack()

    def create_widgets(self):
        self.style = AppStyle()
        self.style.create_label_style("Data.TLabel", font = "Franklin Gothic Medium", background="#252330", foreground="#F5F9F8")

        self.chart_frame = ttk.Frame(self)
        self.chart_frame.pack()

        self.charts_label = ttk.Label(self.chart_frame, text="Charts", style="Data.TLabel")
        self.charts_label.pack(pady=60)
        
        self.canvas = ttk.Canvas(self.chart_frame)
        self.canvas.pack()

        self.canvas = FigureCanvasTkAgg(self.chart_frame, self.canvas)
        

        self.title_label = ttk.Label(self, text="Analytics")
        self.title_label.pack(pady=60)
