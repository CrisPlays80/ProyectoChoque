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
    def __init__(self, parent, connect_db):
        super().__init__(parent, bg="#252330")  # Crea el marco con un fondo oscuro
        self.velocidad, self.orientacion, self.triage = [], [], [] # Almacena los datos de la base de datos
        self.connect_db = connect_db  # Almacena la instancia de la base de datos
        self.create_widgets()  # Crea los elementos de la interfaz
        self.pack(expand=True, fill="both")  # Expande el marco para que ocupe todo el espacio disponible
        
        self.fig = Figure(figsize=(5, 4), dpi=100)
        self.ax = self.fig.add_subplot(111)  # Inicializa el eje

        # Agrega la figura a un widget de Tkinter
        self.canvas = FigureCanvasTkAgg(self.fig, self)
        self.canvas.get_tk_widget().place(x=500, y=100)

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
        self.tree = ttk.Treeview(self, columns=("column1", "column2", "column4"), show="headings", height=20, style="Data.Treeview")
        self.tree.heading("column1", text="Velocidad")
        self.tree.heading("column2", text="Orientacion")
        self.tree.heading("column4", text="Triage")
        self.tree.column("column1", width=100, anchor="center")
        self.tree.column("column2", width=100, anchor="center")
        self.tree.column("column4", width=100, anchor="center")
        self.tree.place(x=40, y=100)

        # Crea una barra de desplazamiento para el árbol
        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.scrollbar.set)

        # Ajusta la posición de la barra de desplazamiento
        tree_width = self.tree.winfo_reqwidth()
        self.scrollbar.place(x=40 + tree_width, y=100, height=self.tree.winfo_reqheight())

        self.show_data()  # Muestra los datos en el árbol

        # ComboBox para seleccionar el tipo de gráfico
        self.graph_type = StringVar()
        self.graph_combobox = ttk.Combobox(self, textvariable=self.graph_type, values=["Velocidad vs Triage", "Orientación vs Velocidad", 'Histograma solo de Triage', 'Gráfica de pastel de Triage'], state="readonly")
        self.graph_combobox.set("Velocidad vs Triage")
        self.graph_combobox.place(x=700, y=80, width=160)
        self.graph_combobox.bind("<<ComboboxSelected>>", self.update_graph)

        # Crear área de la gráfica
        self.create_graph_area()

        # Botones de ordenamiento (por ejemplo, para ordenar por velocidad)
        self.sort_box = ttk.Combobox(self, values=["Velocidad (Asc)", " Velocidad (Des)", "Orientación", 'Orientación (Des)', "Triage", 'Triage (Des)'], state="readonly")
        self.sort_box.set("Ordenar por...")
        self.sort_box.place(x=220, y=70, width=160)
        self.sort_box.bind("<<ComboboxSelected>>", self.sort_table)

    def create_graph_area(self):
        """
        Crear el área de gráficos usando matplotlib.
        """
        self.fig = Figure(figsize=(5, 4), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)  
        self.canvas.draw()
        self.canvas.get_tk_widget().place(x=500, y=100)  # Coloca la gráfica al lado de la tabla

    def show_data(self):
        """
        Mostrar los datos en la tabla desde la base de datos.
        """
        if self.connect_db:
            cursor = self.connect_db.cursor()
            cursor.execute("SELECT velocity, orientation FROM DATA_INFO")  # Ya no seleccionamos 'Accidente'
            rows = cursor.fetchall()

            self.tree.delete(*self.tree.get_children())
            for row in rows:
                self.velocidad.append(row[0])
                self.orientacion.append(row[1])
                self.tree.insert('', 'end', values=(row[0], row[1], clasificar_triage(row[0], row[1])))
                self.triage.append(clasificar_triage(row[0], row[1]))

            cursor.close()

    def sort_table(self, event):
        """
        Ordenar la tabla y los datos dependiendo de la selección en el ComboBox.
        """
        option = self.sort_box.get()
        data_tuples = list(zip(self.velocidad, self.orientacion, self.triage))

        if "Velocidad" in option:
            sorted_data = merge_sort(data_tuples, key_index=0, reverse="(Des)" in option)
        elif "Orientación" in option:
            sorted_data = merge_sort(data_tuples, key_index=1, reverse="(Des)" in option)
        elif "Triage" in option:
            sorted_data = merge_sort(data_tuples, key_index=2, reverse="(Des)" in option)

        self.velocidad, self.orientacion, self.triage = zip(*sorted_data)
        # Actualizar tabla con el orden
        self.tree.delete(*self.tree.get_children())
        for i in range(len(self.velocidad)):
            self.tree.insert('', 'end', values=(self.velocidad[i], self.orientacion[i], self.triage[i]))

    def update_graph(self, event=None):
        """
        Actualizar el gráfico dependiendo de la selección en el ComboBox.
        """
        self.ax.clear()
        graph_type = self.graph_combobox.get()

        if graph_type == "Velocidad vs Triage":
            self.ax.scatter(self.velocidad, self.triage, color='b', marker='o', label="Triage")
            self.ax.set_title("Relación entre Velocidad y Nivel de Triage")
            self.ax.set_xlabel("Velocidad")
            self.ax.set_ylabel("Triage")
        elif graph_type == "Orientación vs Velocidad":
            self.ax.scatter(self.orientacion, self.velocidad, color='r', marker='o', label="Velocidad")
            self.ax.set_title("Relación entre Orientación y Velocidad")
            self.ax.set_xlabel("Orientación")
            self.ax.set_ylabel("Velocidad")
        elif graph_type == 'Histograma solo de Triage':
            self.ax.hist(self.triage, bins=5, color='b', alpha=0.7, rwidth=0.85)
            self.ax.set_title("Histograma de Triage")
            self.ax.set_xlabel("Triage")
            self.ax.set_ylabel("Frecuencia")
            self.ax.set_xlim(1, 5)  # Limita el rango del Triage
            self.ax.set_xticks([1, 2, 3, 4, 5])
        elif graph_type == 'Gráfica de pastel de Triage':
            triage_counts = {i: self.triage.count(i) for i in set(self.triage)}
            
            labels = [f'Triage {k}' for k in triage_counts.keys()]
            sizes = triage_counts.values()
            colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#ffb3e6']

            self.ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
            self.ax.set_title('Distribución de Triage')

        self.ax.legend()
        self.canvas.draw()