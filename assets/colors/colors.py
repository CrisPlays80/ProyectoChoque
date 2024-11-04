import tkinter as tk
from tkinter import ttk
from tkinter import font as tkfont

class AppStyle:
    def __init__(self, theme="default"):
        self.style = ttk.Style()
        self.style.theme_use(theme)
        
        # Carga la fuente personalizada desde el archivo TTF
        self.custom_font_path = "assets/fonts/NotoSans.ttf"
        try:
            self.custom_font = tkfont.Font(family="NotoSans", size=16)
        except tk.TclError:
            # Si no se encuentra la fuente, utiliza una fuente predeterminada
            self.custom_font = tkfont.Font(family="Arial", size=16)
        
    def create_treeview_style(self, style_name, font=None, font_size=16, background="red", foreground="black"):
        font = font or self.custom_font  # Usa la fuente personalizada si no se especifica otra
        self.style.configure(style_name, 
                            font=tkfont.Font(family=font, size=font_size), 
                            background=background, 
                            foreground=foreground,
                            fieldbackground=background)

    def create_button_style(self, style_name, font=None, font_size=16, background="#3B3A4A", foreground="#F5F9F8", borderwidth=0):
        font = font or self.custom_font  # Usa la fuente personalizada si no se especifica otra
        self.style.configure(style_name, 
                            font=tkfont.Font(family=font, size=font_size), 
                            background=background, 
                            foreground=foreground,
                            borderwidth=borderwidth,  # Corrección de typo en 'borderwidth'
                            relief='flat')
        
        # Asegura que el estilo del botón cambie cuando está activo o presionado
        self.style.map(style_name,
            background=[('active', '#3B3A4A'), ('pressed', '#3B3A4A')],
            relief=[('pressed', 'flat')])

    def create_label_style(self, style_name, font=None, font_size=16, background="red", foreground="black"):
        font = font or self.custom_font  # Usa la fuente personalizada si no se especifica otra
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
