from functions.process_data import merge_sort
from functions.consultas import Consultas
from functions.calcular_triage import clasificar_triage

import tkinter as tk
from tkinter import ttk

class Data(tk.Frame):
    def __init__(self, parent, style, ids, velocidad, orientacion, triage, is_admin, connection_db):
        super().__init__(parent, bg="#252330")  # Crea el marco con un fondo oscuro
        self.ids, self.velocidad, self.orientacion, self.triage = ids, velocidad, orientacion, triage # Almacena los datos de la base de datos # Almacena la instancia de la base de datos
        self.style = style  # Crea un objeto de estilo para personalizar la apariencia
        self.enable_button = is_admin
        self.consultas = Consultas(connection_db)
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
        self.title_label.place(x=60, y=40)

        # Crea estilos personalizados para el árbol
        self.style.create_treeview_style("Data.Treeview", background="#252330", foreground="#F5F9F8")
        self.style.create_treeview_style("Data.Treeview.Heading", background="#252330", foreground="#F5F9F8")

        # Crea un árbol para mostrar los datos
        self.tree = ttk.Treeview(self, columns=("column_ID", "column1", "column2", "column4"), show="headings", height=20, style="Data.Treeview")
        
        self.tree.heading("column_ID", text="ID")
        self.tree.column("column_ID", width=0, anchor="center", stretch=tk.NO)

        self.tree.heading("column1", text="Velocidad")
        self.tree.heading("column2", text="Orientacion")
        self.tree.heading("column4", text="Triage")
        self.tree.column("column1", width=180, anchor="center")
        self.tree.column("column2", width=180, anchor="center")
        self.tree.column("column4", width=180, anchor="center")
        self.tree.place(x=40, y=90)

        # Crea una barra de desplazamiento para el árbol
        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.scrollbar.set)

        # Ajusta la posición de la barra de desplazamiento
        tree_width = self.tree.winfo_reqwidth()
        self.scrollbar.place(x=40 + tree_width, y=90, height=self.tree.winfo_reqheight())

        self.show_data()  # Muestra los datos en el árbol

        if self.enable_button:
            self.enable_buttons()

        # Botones de ordenamiento (por ejemplo, para ordenar por velocidad)
        self.sort_box = ttk.Combobox(self, values=["Velocidad ⬆", " Velocidad ⬇", "Orientación ⬆", 'Orientación ⬇', "Triage ⬆", 'Triage ⬇'], state="readonly")
        self.sort_box.set("Ordenar por...")
        self.sort_box.place(x=241, y=50, width=180, height=25)
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
        self.triage_explain_label.place(x=640, y=90)

    def show_data(self):
        for i in range(len(self.velocidad)):
            self.tree.insert('', 'end', values=(self.ids[i], self.velocidad[i], self.orientacion[i], self.triage[i]))

    def sort_table(self, event):
        """
        Ordenar la tabla y los datos dependiendo de la selección en el ComboBox.
        """
        option = self.sort_box.get()
        data_tuples = list(zip(self.ids, self.velocidad, self.orientacion, self.triage))

        if "Velocidad" in option:
            sorted_data = merge_sort(data_tuples, key_index=1, reverse="⬇" in option)
        elif "Orientación" in option:
            sorted_data = merge_sort(data_tuples, key_index=2, reverse="⬇" in option)
        elif "Triage" in option:
            sorted_data = merge_sort(data_tuples, key_index=3, reverse="⬇" in option)

        # Desempaquetar los datos ordenados
        self.ids, self.velocidad, self.orientacion, self.triage = zip(*sorted_data)
        
        # Actualizar la tabla
        self.tree.delete(*self.tree.get_children())
        for i in range(len(self.velocidad)):
            self.tree.insert('', 'end', values=(self.ids[i], self.velocidad[i], self.orientacion[i], self.triage[i]))
    
    def enable_buttons(self):
        self.style.create_button_style("Data.TButton", foreground="#F5F9F8", background="#3B3A4A", font_size = 14)

        print("Botones habilitados")
        self.modify_button = ttk.Button(self, text="Modificar", command=self.modify_data, style='Data.TButton')
        self.create_button = ttk.Button(self, text="Crear", command=self.create_data, style='Data.TButton')
        self.delete_button = ttk.Button(self, text="Eliminar", command=self.delete_data, style='Data.TButton')
        
        # Posicionar los botones en la interfaz
        self.modify_button.place(x=40, y=540)
        self.create_button.place(x=240,y=540)
        self.delete_button.place(x=440,y=540)
    
    def modify_data(self):
        selected_item = self.tree.selection()  # Selecciona la fila
        if not selected_item:
            print("No se ha seleccionado ninguna fila")
            return
        
        # Obtener valores de la fila seleccionada
        current_values = self.tree.item(selected_item, "values")
        current_id, current_velocidad, current_orientacion, current_triage = current_values
        
        # Crear una ventana emergente con los valores actuales para editar
        self.edit_window = tk.Toplevel(self)
        self.edit_window.title("Modificar Registro")
        
        tk.Label(self.edit_window, text="Velocidad").grid(row=0, column=0)
        velocidad_entry = tk.Entry(self.edit_window)
        velocidad_entry.insert(0, current_velocidad)
        velocidad_entry.grid(row=0, column=1)
        
        tk.Label(self.edit_window, text="Orientación").grid(row=1, column=0)
        orientacion_entry = tk.Entry(self.edit_window)
        orientacion_entry.insert(0, current_orientacion)
        orientacion_entry.grid(row=1, column=1)
        
        # Botón para guardar los cambios
        tk.Button(self.edit_window, text="Guardar", command=lambda: self.save_modification(selected_item, current_id, velocidad_entry, orientacion_entry)).grid(row=3, column=0, columnspan=2)

    def save_modification(self, item, current_id, current_velocidad, current_orientacion):
        # Nuevos valores
        new_velocidad = current_velocidad.get()
        new_orientacion =current_orientacion.get() 
        new_triage = clasificar_triage(current_velocidad.get(), current_orientacion.get())
        
        if new_velocidad or new_orientacion or new_triage:
            new_values = (current_id, new_velocidad, new_orientacion, new_triage)
            print(new_values)
            self.tree.item(item, values=new_values)
        
        # Actualizar en la base de datos
        query = """UPDATE DATA_INFO SET velocity = ?, orientation = ? WHERE Id = ?"""
        parametros = (new_velocidad, new_orientacion, current_id)
        self.consultas.actualizar_registro_en_db(query, parametros)
        
        # Actualizar en el Treeview
        self.tree.item(item, values=new_values)

        self.edit_window.destroy()

    def create_data(self):
        self.create_window = tk.Toplevel(self)
        self.create_window.title("Crear Registro")
        
        tk.Label(self.create_window, text="Velocidad").grid(row=0, column=0)
        velocidad_entry = tk.Entry(self.create_window)
        velocidad_entry.grid(row=0, column=1)
        
        tk.Label(self.create_window, text="Orientación").grid(row=1, column=0)
        orientacion_entry = tk.Entry(self.create_window)
        orientacion_entry.grid(row=1, column=1)
        
        # Botón para guardar el nuevo registro
        tk.Button(self.create_window, text="Guardar", command=lambda: self.save_new_data(velocidad_entry, orientacion_entry)).grid(row=3, column=0, columnspan=2)

    def save_new_data(self, current_velocidad, current_orientacion):
        # Nuevos valores
        new_velocidad = current_velocidad.get()
        new_orientacion =current_orientacion.get() 
        new_triage = clasificar_triage(current_velocidad.get(), current_orientacion.get())
        
        if new_velocidad and new_orientacion and new_triage:
            query = """INSERT INTO DATA_INFO (velocity, orientation) VALUES (?, ?)"""
            parametros = (new_velocidad, new_orientacion)
            new_id = self.consultas.guardar_en_db(query, parametros)
            new_values = (new_id, new_velocidad, new_orientacion, new_triage)
            self.tree.insert('', 'end', values=new_values)
            
        self.create_window.destroy()

    def delete_data(self):
        selected_item = self.tree.selection()  # Selecciona la fila
        if not selected_item:
            print("No se ha seleccionado ninguna fila para eliminar")
            return
        
        # Obtener valores de la fila seleccionada (puedes usar el ID si está disponible)
        item_values = self.tree.item(selected_item, 'values')
        
        # Supongamos que tienes un ID único para cada registro
        id_registro = item_values[0]  
        
        # Eliminar el registro de la base de datos
        query = """DELETE FROM DATA_INFO WHERE Id = ?"""
        self.consultas.eliminar_de_db(query, (id_registro,))
        
        # Eliminar la fila del Treeview
        self.tree.delete(selected_item)
        print(f"Registro con valores {item_values} eliminado")

    def generate_new_id(self):
        # Obtener el ID más alto de la base de datos y sumarle 1
        query = "SELECT MAX(id) FROM tu_tabla"
        self.cursor.execute(query)
        max_id = self.cursor.fetchone()[0]
        
        if max_id is None:
            return 1  # Si no hay registros en la tabla, empieza en 1
        return max_id + 1