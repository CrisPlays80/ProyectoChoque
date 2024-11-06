from assets.colors.colors import AppStyle  # Importa el estilo personalizado para los elementos de la interfaz
from functions.calcular_triage import clasificar_triage
from functions.process_data import merge_sort

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from tkinter import StringVar

class Data(tk.Frame):
    def __init__(self, parent, style, velocidad, orientacion, triage):
        super().__init__(parent, bg="#252330")  # Crea el marco con un fondo oscuro
        self.velocidad, self.orientacion, self.triage = velocidad, orientacion, triage # Almacena los datos de la base de datos # Almacena la instancia de la base de datos
        self.style = style  # Crea un objeto de estilo para personalizar la apariencia
        self.create_widgets()  # Crea los elementos de la interfaz
        self.pack(expand=True, fill="both")  # Expande el marco para que ocupe todo el espacio disponible

    def create_widgets(self):
        """
        Crea los elementos de la interfaz del marco.
        """

        # Crea un estilo personalizado para las etiquetas
        self.style.create_label_style("Data.TLabel", background="#252330", foreground="#F5F9F8")

        # Crea una etiqueta de título
        self.title_label = ttk.Label(self, text="Analytics", style="Data.TLabel")
        self.title_label.place(x=60, y=50)

        # Crea estilos personalizados para el árbol
        self.style.create_treeview_style("Data.Treeview", background="#252330", foreground="#F5F9F8")
        self.style.create_treeview_style("Data.Treeview.Heading", background="#252330", foreground="#F5F9F8")

        # Crea un árbol para mostrar los datos
        self.tree = ttk.Treeview(self, columns=("column1", "column2", "column4"), show="headings", height=20, style="Data.Treeview")
        self.tree.heading("column1", text="Velocidad", )
        self.tree.heading("column2", text="Orientacion")
        self.tree.heading("column4", text="Triage")
        self.tree.column("column1", width=180, anchor="center")
        self.tree.column("column2", width=180, anchor="center")
        self.tree.column("column4", width=180, anchor="center")
        self.tree.place(x=40, y=100)

        # Crea una barra de desplazamiento para el árbol
        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.scrollbar.set)

        # Ajusta la posición de la barra de desplazamiento
        tree_width = self.tree.winfo_reqwidth()
        self.scrollbar.place(x=40 + tree_width, y=100, height=self.tree.winfo_reqheight())

        self.show_data()  # Muestra los datos en el árbol

        # Botones de ordenamiento (por ejemplo, para ordenar por velocidad)
        self.sort_box = ttk.Combobox(self, values=["Velocidad ⬆", " Velocidad ⬇", "Orientación ⬆", 'Orientación ⬇', "Triage ⬆", 'Triage ⬇'], state="readonly")
        self.sort_box.set("Ordenar por...")
        self.sort_box.place(x=241, y=60, width=180, height=25)
        self.sort_box.bind("<<ComboboxSelected>>", self.sort_table)

        self.triage_explain_label = tk.Label(self, 
                                text="""Clasificacion de triaje
1-Rojo(Emergencia): Pacientes en condiciones críticas que necesitan 
atención inmediata, como paros cardíacos, traumas severos, heridas 
que arriesguen la vida del paciente o dificultad respiratoria aguda.
La atención debe ser inmediata.

2-Naranja(Muy urgente): Para condiciones graves que requieren tratamiento 
rápido pero no son de riesgo inminente de muerte. Entre estos se incluye 
fracturas complejas y heridas profundas. 
El tiempo ideal de espera para su atención es de menos de 30 minutos

3-Amarillo(Urgencia menor): Casos que no son graves pero requieren atención 
médica en un plazo corto, como dolores intensos que no sean críticos 
o infecciones agudas. 
El tiempo de espera para su atención es de hasta 1 hora.

4-Verde(No Urgente): Condiciones leves, como resfriados o lesiones menores,
que pueden esperar más tiempo. 
El tiempo de espera en su atención puede ser de varias horas

5-Azul(Sin Urgencia): Casos que no requieren tratamiento inmediato y pueden 
atenderse en consulta externa o en otras áreas menos especializadas.""",
                                bg="#252330", fg="#F5F9F8", font=("CreatoDisplay-Regular", 12),
                                justify="left",  # Justifica el texto al centro
                                anchor="center")
        self.triage_explain_label.place(x=640, y=100)

    def show_data(self):
        for i in range(len(self.velocidad)):
            self.tree.insert('', 'end', values=(self.velocidad[i], self.orientacion[i], self.triage[i]))

    def sort_table(self, event):
        """
        Ordenar la tabla y los datos dependiendo de la selección en el ComboBox.
        """
        option = self.sort_box.get()
        data_tuples = list(zip(self.velocidad, self.orientacion, self.triage))

        if "Velocidad" in option:
            sorted_data = merge_sort(data_tuples, key_index=0, reverse="⬇" in option)
        elif "Orientación" in option:
            sorted_data = merge_sort(data_tuples, key_index=1, reverse="⬇" in option)
        elif "Triage" in option:
            sorted_data = merge_sort(data_tuples, key_index=2, reverse="⬇" in option)

        # Desempaquetar los datos ordenados
        self.velocidad, self.orientacion, self.triage = zip(*sorted_data)
        
        # Actualizar la tabla
        self.tree.delete(*self.tree.get_children())
        for i in range(len(self.velocidad)):
            self.tree.insert('', 'end', values=(self.velocidad[i], self.orientacion[i], self.triage[i]))