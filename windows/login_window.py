from assets.colors.colors import AppStyle
from frame import RoundedFrame

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox  # Usamos messagebox para mostrar mensajes de error o confirmación

class LoginWindow(tk.Frame):
    def __init__(self, parent, connect_db, username_callback):
        super().__init__(parent, bg='#252330')
        self.username_callback = username_callback
        self.connect_db = connect_db
        self.create_widgets()

    def create_widgets(self):
        # Crear una instancia de AppStyle para definir los estilos de la interfaz
        self.style = AppStyle()
        self.style.create_label_style("LoginWindow.TLabel", font="Helvetica", background="#525167", foreground="white")
        self.style.create_button_style("LoginWindow.TButton", font="Helvetica", background="#3B3A4A", foreground="white")
        
        self.rounded_frame = RoundedFrame(self, width=1200, height=620, corner_radius=100, color='#3B3A4A')
        self.rounded_frame.pack(pady=40)
        
        self.welcome_frame(self.rounded_frame)
        self.login_frame(self.rounded_frame)

    def welcome_frame(self, parent):
        self.welcome_text = tk.Frame(parent, bg='#3B3A4A', width=400, height=400, highlightthickness=0)
        self.welcome_text.place(x=100, y=110)

        # Etiqueta de bienvenida
        self.welcome_label = tk.Label(self.welcome_text, text="Welcome!", background="#3B3A4A",foreground="white", font=("Helvetica", 40, "bold"))
        self.welcome_label.place(x=40, y=40)

        # Etiqueta de descripción
        self.description_label = tk.Label(self.welcome_text, text="We are happy to see you", background="#3B3A4A",foreground="white", font=("Helvetica", 16))
        self.description_label.place(x=40, y=100)

        # Etiqueta de instrucciones

    def login_frame(self, parent):
        self.login_text = tk.Frame(parent, bg='#525167', width=400, height=400, highlightthickness=0)
        self.login_text.place(x=700, y=110)
        # Etiqueta "Username" (Nombre de usuario)
        self.username_label = ttk.Label(self.login_text, text="Username:", style="LoginWindow.TLabel")
        self.username_label.place(x=40, y=40)

        # Campo de entrada para el nombre de usuario
        self.username_str = tk.StringVar()  # Se utiliza StringVar para vincular el texto del campo de entrada
        self.username_entry = ttk.Entry(self.login_text, textvariable=self.username_str)
        self.username_entry.place(x=40, y=70, width=220)

        # Etiqueta "Password" (Contraseña)
        self.password_label = ttk.Label(self.login_text, text="Password:", style="LoginWindow.TLabel")
        self.password_label.place(x=40, y=120)

        # Campo de entrada para la contraseña, con máscara de texto ("*")
        self.password_str = tk.StringVar()  # Se utiliza StringVar para vincular el texto del campo de entrada
        self.password_entry = ttk.Entry(self.login_text, show="*", textvariable=self.password_str)
        self.password_entry.place(x=40, y=150, width=220)

        # Botón de "Register" (Registro)
        self.register_button = ttk.Button(self.login_text, text="Register", command=self.register, style="LoginWindow.TButton")
        self.register_button.place(x=60, y=220, width=80)

        # Botón de "Login"
        self.login_button = ttk.Button(self.login_text, text="Login", command=self.login, style="LoginWindow.TButton")
        self.login_button.place(x=160, y=220, width=80)

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
                if password == user[2]:  # Verificamos si la contraseña coincide
                    messagebox.showinfo("Login exitoso", f"¡Bienvenido {username}!")
                    self.username_callback(username)
                else:
                    # Si la contraseña no coincide, mostramos un mensaje de error
                    messagebox.showerror("Error", "Contraseña incorrecta")
            else:
                # Si el usuario no existe, mostramos un mensaje indicando que debe registrarse
                messagebox.showerror("Error", "Usuario no encontrado. Por favor, regístrese.")
            
            # Cerramos el cursor y la conexión a la base de datos
            cursor.close()