import tkinter as tk
from tkinter import ttk
from tkinter import font as tkfont
import os
from PIL import ImageFont
from fontTools.ttLib import TTFont

class AppStyle:
    def __init__(self, theme="default"):
        self.style = ttk.Style()
        self.style.theme_use(theme)
        
        # Ruta de la fuente
        self.custom_font_path = os.path.join("assets/fonts/CreatoDisplay-Regular.otf")
        
        # Cargar la fuente dinámicamente
        try:
            # Cargar e instalar la fuente temporalmente
            font_loaded = self.load_custom_font(self.custom_font_path)
            if font_loaded:
                self.custom_font = tkfont.Font(family="CreatoDisplay-Regular", size=16)
                print("Fuente cargada exitosamente")
            else:
                print("No se pudo cargar la fuente, usando Arial")
                self.custom_font = tkfont.Font(family="Arial", size=16)
        except Exception as e:
            print(f"Error al cargar la fuente: {e}")
            self.custom_font = tkfont.Font(family="Arial", size=16)

    def load_custom_font(self, font_path):
        try:
            # Verificar si la fuente existe
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
            
            # Crear directorio temporal para la fuente
            temp_dir = Path(tempfile.gettempdir()) / "custom_fonts"
            temp_dir.mkdir(exist_ok=True)
            
            # Copiar la fuente al directorio temporal
            font_temp_path = temp_dir / Path(font_path).name
            shutil.copy2(font_path, font_temp_path)
            
            # En Windows
            if os.name == 'nt':
                import ctypes
                from ctypes import wintypes
                GR_FONT_RESOURCE = 1
                FR_PRIVATE = 0x10
                AddFontResourceEx = ctypes.windll.gdi32.AddFontResourceExW
                AddFontResourceEx.restype = wintypes.HANDLE
                AddFontResourceEx.argtypes = [wintypes.LPCWSTR, wintypes.DWORD, ctypes.c_void_p]
                AddFontResourceEx(str(font_temp_path), FR_PRIVATE, None)
            
            return True
            
        except Exception as e:
            print(f"Error al cargar la fuente: {e}")
            return False

    def create_treeview_style(self, style_name, font=None, font_size=16, background="white", foreground="black"):
        """
        Crea un estilo personalizado para Treeview
        """
        if font is None:
            font = self.custom_font

        # Estilo principal del Treeview
        self.style.configure(
            style_name,
            font=(font.actual()['family'], font_size),
            background=background,
            foreground=foreground,
            fieldbackground=background
        )

        # Estilo para el encabezado del Treeview
        self.style.configure(
            f"{style_name}.Heading",
            font=(font.actual()['family'], font_size),
            background=background,
            foreground=foreground
        )

        # Estilo para los elementos seleccionados
        self.style.map(
            style_name,
            background=[('selected', '#0078D7')],
            foreground=[('selected', 'white')]
        )

    def create_button_style(self, style_name, font=None, font_size=16, background="#3B3A4A", 
                        foreground="#F5F9F8", borderwidth=0):
        """
        Crea un estilo personalizado para botones
        """
        if font is None:
            font = self.custom_font
            
        self.style.configure(
            style_name,
            font=(font.actual()['family'], font_size),
            background=background,
            foreground=foreground,
            borderwidth=borderwidth,
            relief='flat',
        )
        
        self.style.map(
            style_name,
            background=[('active', '#4A4959'), ('pressed', '#2D2C3A')],
            foreground=[('active', '#FFFFFF'), ('pressed', '#E0E0E0')],
            relief=[('pressed', 'flat')]
        )

    def create_label_style(self, style_name, font=None, font_size=16, background="white", 
                        foreground="#F5F9F8"):
        """
        Crea un estilo personalizado para etiquetas
        """
        if font is None:
            font = self.custom_font
            
        self.style.configure(
            style_name,
            font=(font.actual()['family'], font_size),
            background=background,
            foreground=foreground,
        )

    def create_entry_style(self, style_name, font=None, font_size=16, 
                        background="white", 
                        foreground="#333333",
                        fieldbackground="#696783",
                        bordercolor="#E0E0E0",  
                        focuscolor="#2196F3",   
                        padding=(12, 8)):        # Padding aumentado para forma más redondeada
        """
        Crea un estilo personalizado para entries redondeados
        """
        if font is None:
            font = self.custom_font
            
        self.style.configure(
            style_name,
            font=(font.actual()['family'], font_size),
            background=background,
            foreground=foreground,
            fieldbackground=fieldbackground,
            borderwidth=0,
            relief="solid",
            padding=padding
        )

        # Efecto focus
        self.style.map(
            style_name,
            bordercolor=[('focus', focuscolor)],
            lightcolor=[('focus', focuscolor)],
            darkcolor=[('focus', focuscolor)]
        )

    def create_frame_style(self, style_name, background="#F0F0F0", borderwidth=0, relief="flat"):
        """
        Crea un estilo personalizado para frames
        """
        self.style.configure(
            style_name,
            background=background,
            borderwidth=borderwidth,
            relief=relief
        )

    def create_notebook_style(self, style_name, font=None, font_size=16, background="#F0F0F0", 
                            selected_background="#FFFFFF", padding=(5, 2)):
        """
        Crea un estilo personalizado para notebooks (pestañas)
        """
        if font is None:
            font = self.custom_font
            
        self.style.configure(
            style_name,
            font=(font.actual()['family'], font_size),
            background=background,
            padding=padding
        )
        
        # Estilo para las pestañas
        self.style.configure(
            f"{style_name}.Tab",
            font=(font.actual()['family'], font_size),
            background=background,
            padding=padding
        )
        
        self.style.map(
            f"{style_name}.Tab",
            background=[('selected', selected_background)],
            expand=[('selected', [1, 1, 1, 0])]
        )

    def apply_style(self, widget, style_name):
        """
        Aplica un estilo a un widget
        """
        if isinstance(widget, (ttk.Button, ttk.Label, ttk.Entry, ttk.Frame, 
                            ttk.Notebook, ttk.Treeview)):
            widget.configure(style=style_name)
        else:
            print(f"Advertencia: El widget {type(widget)} no es compatible con estilos ttk")

    def get_font(self):
        """
        Retorna la fuente personalizada actual
        """
        return self.custom_font

    def set_font_size(self, size):
        """
        Cambia el tamaño de la fuente personalizada
        """
        self.custom_font.configure(size=size)