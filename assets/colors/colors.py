import tkinter as tk
from tkinter import ttk
from tkinter import font as tkfont
import os
from fontTools.ttLib import TTFont

class AppStyle:
    _font_loaded = False  # Variable de clase para verificar si la fuente ya fue cargada

    def __init__(self, theme="default"):
        self.style = ttk.Style()
        self.style.theme_use(theme)

        # Ruta de la fuente
        self.custom_font_path = os.path.join("assets/fonts/CreatoDisplay-Regular.otf")

        # Cargar la fuente solo una vez
        if not AppStyle._font_loaded:
            font_loaded = self.load_custom_font(self.custom_font_path)
            if font_loaded:
                self.custom_font = tkfont.Font(family="CreatoDisplay-Regular", size=16)
                print("Fuente cargada exitosamente")
            else:
                print("No se pudo cargar la fuente, usando Arial")
                self.custom_font = tkfont.Font(family="Arial", size=16)
            AppStyle._font_loaded = True

    def load_custom_font(self, font_path):
        try:
            if not os.path.exists(font_path):
                return False

            # Cargar la fuente usando fontTools
            font = TTFont(font_path)
            font_family = font['name'].getName(1, 3, 1, 1033).string
            if isinstance(font_family, bytes):
                font_family = font_family.decode('utf-8')

            # Registrar la fuente en el sistema
            import tempfile
            import shutil
            from pathlib import Path
            
            temp_dir = Path(tempfile.gettempdir()) / "custom_fonts"
            temp_dir.mkdir(exist_ok=True)

            # Copiar la fuente al directorio temporal
            font_temp_path = temp_dir / Path(font_path).name
            shutil.copy2(font_path, font_temp_path)

            if os.name == 'nt':
                import ctypes
                from ctypes import wintypes
                AddFontResourceEx = ctypes.windll.gdi32.AddFontResourceExW
                AddFontResourceEx.restype = wintypes.HANDLE
                AddFontResourceEx.argtypes = [wintypes.LPCWSTR, wintypes.DWORD, ctypes.c_void_p]
                AddFontResourceEx(str(font_temp_path), 0x10, None)
            
            return True
        except Exception as e:
            print(f"Error al cargar la fuente: {e}")
            return False

    def create_treeview_style(self, style_name, font=None, font_size=16, background="white", foreground="black"):
        if font is None:
            font = self.custom_font
        self.style.configure(style_name,
                            font=(font.actual()['family'], font_size),
                            background=background,
                            foreground=foreground,
                            fieldbackground=background)
        self.style.map(style_name,
                    background=[('selected', '#0078D7')],
                    foreground=[('selected', 'white')])

    def create_button_style(self, style_name, font=None, font_size=16, background="#3B3A4A",
                            foreground="#F5F9F8", borderwidth=0, tipo = 'bold'):
        if font is None:
            font = self.custom_font
        self.style.configure(style_name,
                            font=(font.actual()['family'], font_size, tipo),
                            background=background,
                            foreground=foreground,
                            borderwidth=borderwidth,
                            relief='flat')
        self.style.map(style_name,
                    background=[('active', '#4A4959'), ('pressed', '#2D2C3A')],
                    foreground=[('active', '#FFFFFF'), ('pressed', '#E0E0E0')],
                    relief=[('pressed', 'flat')])

    def create_label_style(self, style_name, font=None, font_size=16, background="white", foreground="#F5F9F8"):
        if font is None:
            font = self.custom_font
        self.style.configure(style_name,
                            font=(font.actual()['family'], font_size),
                            background=background,
                            foreground=foreground)

    def create_entry_style(self, style_name, font=None, font_size=16, background="white",
                        foreground="#333333", fieldbackground="#696783", bordercolor="#E0E0E0",
                        focuscolor="#2196F3", padding=(12, 8)):
        if font is None:
            font = self.custom_font
        self.style.configure(style_name,
                            font=(font.actual()['family'], font_size),
                            background=background,
                            foreground=foreground,
                            fieldbackground=fieldbackground,
                            borderwidth=0,
                            relief="solid",
                            padding=padding)
        self.style.map(style_name,
                    bordercolor=[('focus', focuscolor)],
                    lightcolor=[('focus', focuscolor)],
                    darkcolor=[('focus', focuscolor)])

    def create_frame_style(self, style_name, background="#F0F0F0", borderwidth=0, relief="flat"):
        self.style.configure(style_name, background=background, borderwidth=borderwidth, relief=relief)

    def create_notebook_style(self, style_name, font=None, font_size=16, background="#F0F0F0",
                            selected_background="#FFFFFF", padding=(5, 2)):
        if font is None:
            font = self.custom_font
        self.style.configure(style_name,
                            font=(font.actual()['family'], font_size),
                            background=background,
                            padding=padding)
        self.style.configure(f"{style_name}.Tab",
                            font=(font.actual()['family'], font_size),
                            background=background,
                            padding=padding)
        self.style.map(f"{style_name}.Tab",
                    background=[('selected', selected_background)],
                    expand=[('selected', [1, 1, 1, 0])])

    def apply_style(self, widget, style_name):
        if isinstance(widget, (ttk.Button, ttk.Label, ttk.Entry, ttk.Frame, ttk.Notebook, ttk.Treeview)):
            widget.configure(style=style_name)
        else:
            print(f"Advertencia: El widget {type(widget)} no es compatible con estilos ttk")

    def get_font(self):
        return self.custom_font

    def set_font_size(self, size):
        self.custom_font.configure(size=size)
