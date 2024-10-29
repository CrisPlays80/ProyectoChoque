from assets.colors.colors import AppStyle  # Importa el estilo personalizado para los elementos de la interfaz
from windows import LoginWindow  # Importa la ventana de inicio de sesión (no utilizada en este fragmento)
from app.connect_db import connect_db  # Importa la función para conectar a la base de datos

import tkinter as tk  # Importa la biblioteca Tkinter para crear interfaces gráficas
from tkinter import ttk  # Importa el módulo ttk para usar widgets temáticos

class Data(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#252330")  # Crea el marco con un fondo oscuro
        self.create_widgets()  # Crea los elementos de la interfaz
        self.pack(expand=True, fill="both")  # Expande el marco para que ocupe todo el espacio disponible

    def show_data(self):
        """
        Obtiene los datos de la base de datos y los muestra en el árbol.
        """
        connect = connect_db()  # Conecta a la base de datos
        if connect:
            cursor = connect.cursor()  # Crea un cursor para ejecutar consultas
            cursor.execute("SELECT * FROM DATA_INFO")  # Ejecuta una consulta para obtener todos los datos
            rows = cursor.fetchall()  # Obtiene todos los resultados de la consulta

            self.tree.delete(*self.tree.get_children())  # Limpia el árbol antes de agregar nuevos datos
            for row in rows:
                self.tree.insert('', 'end', values=(row[0], row[1]))  # Inserta cada fila en el árbol

            cursor.close()  # Cierra el cursor
            connect.close()  # Cierra la conexión a la base de datos

    def create_widgets(self):
        """
        Crea los elementos de la interfaz del marco.
        """
        self.style = AppStyle()  # Crea un objeto de estilo para personalizar la apariencia

        # Crea un estilo personalizado para las etiquetas
        self.style.create_label_style("Data.TLabel", font="Franklin Gothic Medium", background="#252330", foreground="#F5F9F8")

        # Crea una etiqueta de título
        self.title_label = ttk.Label(self, text="Analytics", style="Data.TLabel")
        self.title_label.place(x=60, y=50)

        # Crea estilos personalizados para el árbol
        self.style.create_treeview_style("Data.Treeview", background="#252330", foreground="#F5F9F8")
        self.style.create_treeview_style("Data.Treeview.Heading", background="#252330", foreground="#F5F9F8")

        # Crea un árbol para mostrar los datos
        self.tree = ttk.Treeview(self, columns=("column1", "column2"), show="headings", height=20, style="Data.Treeview")
        self.tree.heading("column1", text="Velocidad")
        self.tree.heading("column2", text="Orientacion")
        self.tree.column("column1", width=300, anchor="center")
        self.tree.column("column2", width=300, anchor="center")
        self.tree.place(x=40, y=100)

        # Crea una barra de desplazamiento para el árbol
        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.scrollbar.set)

        # Ajusta la posición de la barra de desplazamiento
        tree_width = self.tree.winfo_reqwidth()
        self.scrollbar.place(x=40 + tree_width, y=100, height=self.tree.winfo_reqheight())

        self.show_data()  # Muestra los datos en el árbol
        self.update_idletasks()  # Actualiza la disposición de los elementos