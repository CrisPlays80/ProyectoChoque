import tkinter as tk
from tkinter import ttk
from tkinter import font as tkfont


class AppStyle:
    def __init__(self, theme="default"):
        self.style = ttk.Style()
        self.style.theme_use(theme)
        self.custom_font_path = "assets/fonts/NotoSans.ttf"
        self.custom_font = tkfont.Font(family="CustomFont", size=16)
        print("Sexo")

    def create_button_style(self, style_name, font="CustomFont", font_size=36, background="#3B3A4A", foreground="#F5F9F8", borderwidth=0):
        self.style.configure(style_name, 
                            font=tkfont.Font(family=font, size=font_size), 
                            background=background, 
                            foreground=foreground,
                            borderwith= borderwidth,
                            relief='flat'
                            )
        self.style.map("Dashboard.TButton",
          background=[('active', '#3B3A4A'), ('pressed', '#3B3A4A')],
          relief=[('pressed', 'flat')])

    def create_label_style(self, style_name, font="CustomFont", font_size=36, background="red", foreground="black"):
        self.style.configure(style_name, 
                            font=tkfont.Font(family=font, size=font_size), 
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

