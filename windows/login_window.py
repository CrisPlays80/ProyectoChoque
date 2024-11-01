from .base_window import BaseWindow
from assets.colors.colors import AppStyle

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox  # Usamos messagebox para mostrar mensajes de error o confirmación

class LoginWindow(BaseWindow):
    def __init__(self, parent, connect_db, username_callback):
        super().__init__(parent, title="Login", width=400, height=250)
        self.configure(bg="#575669")
        self.resizable(False, False)
        self.username_callback = username_callback
        self.connect_db = connect_db
        self.create_widgets()

    def create_widgets(self):
        # Crear una instancia de AppStyle para definir los estilos de la interfaz
        self.style = AppStyle()
        self.style.create_label_style("LoginWindow.TLabel", font="Helvetica", background="#575669", foreground="white")
        self.style.create_button_style("LoginWindow.TButton", font="Helvetica", background="#3B3A4A", foreground="white")
    
        # Etiqueta "Username" (Nombre de usuario)
        self.username_label = ttk.Label(self, text="Username:", style="LoginWindow.TLabel")
        self.username_label.pack(pady=20)

        # Campo de entrada para el nombre de usuario
        self.username_str = tk.StringVar()  # Se utiliza StringVar para vincular el texto del campo de entrada
        self.username_entry = ttk.Entry(self, textvariable=self.username_str)
        self.username_entry.pack(pady=0)

        # Etiqueta "Password" (Contraseña)
        self.password_label = ttk.Label(self, text="Password:", style="LoginWindow.TLabel")
        self.password_label.pack(pady=20)

        # Campo de entrada para la contraseña, con máscara de texto ("*")
        self.password_str = tk.StringVar()  # Se utiliza StringVar para vincular el texto del campo de entrada
        self.password_entry = ttk.Entry(self, show="*", textvariable=self.password_str)
        self.password_entry.pack(pady=0)

        # Botón de "Register" (Registro)
        self.register_button = ttk.Button(self, text="Register", command=self.register, style="LoginWindow.TButton")
        self.register_button.place(x=90, y=190)  # Posicionamos el botón en la ventana

        # Botón de "Login"
        self.login_button = ttk.Button(self, text="Login", command=self.login, style="LoginWindow.TButton")
        self.login_button.place(x=220, y=190)  # Posicionamos el botón en la ventana
        
    def register(self):
        # Obtener el valor de los campos de usuario y contraseña
        username = self.username_str.get()
        password = self.password_str.get()

        # Si el nombre de usuario o la contraseña están vacíos, mostramos un mensaje de error
        if not username or not password:
            messagebox.showerror("Error", "Por favor ingrese un nombre de usuario y una contraseña")
            return

        # Conexión a la base de datos
        if self.connect_db:
            cursor = self.connect_db.cursor()  # Crear un cursor para ejecutar consultas SQL

            # Verificar si el usuario ya existe en la base de datos
            cursor.execute("SELECT * FROM USERS WHERE username = ?", (username,))
            user = cursor.fetchone()  # Recuperar un solo registro que coincida con el nombre de usuario
            
            if user:
                # Si el usuario ya existe, mostramos un mensaje de error
                messagebox.showerror("Error", "El usuario ya existe")
            else:
                # Si el usuario no existe, lo insertamos en la base de datos
                cursor.execute("INSERT INTO USERS (username, password) VALUES (?, ?)", (username, password))
                self.connect_db.commit()  # Confirmamos los cambios en la base de datos
                messagebox.showinfo("Registro", "Usuario registrado exitosamente")
            
            # Cerramos el cursor y la conexión a la base de datos
            cursor.close()
    
    def login(self):
        # Obtener el valor de los campos de usuario y contraseña
        username = self.username_str.get()
        password = self.password_str.get()

        # Si el nombre de usuario o la contraseña están vacíos, mostramos un mensaje de error
        if not username or not password:
            messagebox.showerror("Error", "Por favor ingrese un nombre de usuario y una contraseña")
            return

        # Conexión a la base de datos
        if self.connect_db:
            cursor = self.connect_db.cursor()  # Crear un cursor para ejecutar consultas SQL

            # Buscar el usuario en la base de datos
            cursor.execute("SELECT * FROM USERS WHERE username = ?", (username,))
            user = cursor.fetchone()  # Recuperar el registro del usuario que coincida
            
            if user:
                # Si el usuario existe, verificamos si la contraseña es correcta
                if password == user[1]:  # Verificamos si la contraseña coincide
                    messagebox.showinfo("Login exitoso", f"¡Bienvenido {username}!")
                    self.username_callback(username)
                    self.destroy()  # Cerramos la ventana de inicio de sesión
                else:
                    # Si la contraseña no coincide, mostramos un mensaje de error
                    messagebox.showerror("Error", "Contraseña incorrecta")
            else:
                # Si el usuario no existe, mostramos un mensaje indicando que debe registrarse
                messagebox.showerror("Error", "Usuario no encontrado. Por favor, regístrese.")
            
            # Cerramos el cursor y la conexión a la base de datos
            cursor.close()