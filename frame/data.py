import numpy as np
from assets.colors.colors import AppStyle
from windows import LoginWindow

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import tkinter as tk
from tkinter import ttk

class Data(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#252330")
        self.create_widgets()
        self.pack(side="left", fill="both", expand=True)

    def create_widgets(self):
        self.style = AppStyle()
        self.style.create_label_style("Data.TLabel", font = "Franklin Gothic Medium", background="#252330", foreground="#F5F9F8")

        self.chart_frame = tk.Frame(self, background="#252330")
        self.chart_frame.pack()

        self.charts_label = ttk.Label(self.chart_frame, text="Charts", style="Data.TLabel")
        self.charts_label.pack(pady=60)

        fig = Figure(figsize=(5, 4), dpi=100)
        t = np.arange(0, 3, .01)
        fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))

        self.canvas = FigureCanvasTkAgg(fig, master=self.chart_frame)
        self.canvas.get_tk_widget().pack()
        

        self.title_label = ttk.Label(self, text="Analytics")
        self.title_label.pack(pady=60)
