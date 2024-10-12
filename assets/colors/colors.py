import tkinter as tk
from tkinter import ttk

class AppStyle:
    def __init__(self, theme="default"):
        self.style = ttk.Style()
        self.style.theme_use(theme)

    def create_button_style(self, style_name, font="Helvetica", font_size=10, background="#3B3A4A", foreground="#F5F9F8"):
        self.style.configure(style_name, 
                            font=(font, font_size, "bold"), 
                            background=background, 
                            foreground=foreground)

    def create_label_style(self, style_name, font="Helvetica", font_size=10, background="red", foreground="black"):
        self.style.configure(style_name, 
                            font=(font, font_size, "bold"), 
                            background=background, 
                            foreground=foreground)

    def create_frame_style(self, style_name, background="#F0F0F0"):
        self.style.configure(style_name, background=background)
    
    def apply_button_style(self, widget, style_name):
        widget.configure(style=style_name)

    def apply_label_style(self, widget, style_name):
        widget.configure(style=style_name)
        
    def apply_frame_style(self, widget, style_name):
        widget.configure(style=style_name)

