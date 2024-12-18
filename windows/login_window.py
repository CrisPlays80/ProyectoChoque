from frame import RoundedFrame

import bcrypt
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk  # Usamos messagebox para mostrar mensajes de error o confirmación

class LoginWindow(tk.Frame):
    def __init__(self, parent, connect_db, username_callback, style):
        super().__init__(parent, bg='#252330')
        self.username_callback = username_callback
        self.connect_db = connect_db
        self.style = style
        self.is_admin = False
        self.create_widgets()

    def create_widgets(self):
        # Crear una instancia de AppStyle para definir los estilos de la interfaz
        self.style.create_label_style("LoginWindow.TLabel", background='#525167')
        self.style.create_button_style("LoginWindow.TButton")
        self.style.create_entry_style("LoginWindow.TEntry")
        
        self.rounded_frame = RoundedFrame(self, width=1200, height=620, corner_radius=100, color='#3B3A4A')
        self.rounded_frame.pack(pady=40)
        
        self.welcome_frame(self.rounded_frame)
        self.login_frame(self.rounded_frame)

    def welcome_frame(self, parent):
        self.welcome_text = tk.Frame(parent, bg='#3B3A4A', width=440, height=400, highlightthickness=0)
        self.welcome_text.place(x=100, y=110)
        # Image
        self.image = Image.open("assets/images/logo.png")
        self.image = self.image.resize((100, 100), Image.Resampling.LANCZOS)
        self.image = ImageTk.PhotoImage(self.image)
        
        # Add Logo
        self.logo = ttk.Label(self, image=self.image, style="Logo.TLabel", background="#3B3A4A")
        self.logo.place(x = 35, y = 80)
        
        # Etiqueta de bienvenida
        self.welcome_label = tk.Label(self.welcome_text, text="Bienvenidos!", background="#3B3A4A",foreground="white", font=("CreatoDisplay-Bold", 52))
        self.welcome_label.place(x=5, y = 80)

        self.line = ttk.Separator(self.welcome_text, orient="horizontal")
        self.line.place(x=10, y=230, width=200, height=3)

        # Etiqueta de descripción
        self.multiline_label = tk.Label(self.welcome_text, 
                                text="Decisiones médicas más rápidas, mejores resultados.\nTriageCare tu aliado en la atención médica de emergencia.",
                                bg="#3B3A4A", fg="white", font=("CreatoDisplay-Regular", 13),
                                justify="left",  # Justifica el texto al centro
                                anchor="center")  
        self.multiline_label.place(x=5, y=320)

        # Etiqueta de instrucciones

    def login_frame(self, parent):
        self.style.create_button_style("LoginWindow.TButton")
        self.style.create_entry_style("LoginWindow.TEntry")
        self.login_text = tk.Frame(parent, bg='#525167', width=400, height=400, highlightthickness=0)
        self.login_text.place(x=700, y=110)

        self.sign_label = tk.Label(self.login_text, text="TriageCare", font=("CreatoDisplay-Bold", 32), background="#525167",foreground="white")
        self.sign_label.place(x=80, y=35)

        # Etiqueta "Username" (Nombre de usuario)
        self.username_label = ttk.Label(self.login_text, text="Username", style="LoginWindow.TLabel")
        self.username_label.place(x=60, y=110)

        # Campo de entrada para el nombre de usuario
        self.username_str = tk.StringVar()  # Se utiliza StringVar para vincular el texto del campo de entrada
        self.username_entry = ttk.Entry(self.login_text, textvariable=self.username_str, style="LoginWindow.TEntry")
        self.username_entry.place(x=60, y=140, width=280)

        # Etiqueta "Password" (Contraseña)
        self.password_label = ttk.Label(self.login_text, text="Password", style="LoginWindow.TLabel")
        self.password_label.place(x=60, y=190)

        # Campo de entrada para la contraseña, con máscara de texto ("*")
        self.password_str = tk.StringVar()  # Se utiliza StringVar para vincular el texto del campo de entrada
        self.password_entry = ttk.Entry(self.login_text, show="*", textvariable=self.password_str, style="LoginWindow.TEntry")
        self.password_entry.place(x=60, y=220, width=280)

        # Etiqueta "Adviser" (Asesor)
        self.informant_str = tk.StringVar()
        self.informant_label = tk.Label(self.login_text, text="", textvariable=self.informant_str, font=("CreatoDisplay-Regular", 12), background="#525167",foreground="#F5F9F8")
        self.informant_label.place(x=52, y=270)

        # Botón de "Register" (Registro)
        self.register_button = ttk.Button(self.login_text, text="Register", command=self.register, style="LoginWindow.TButton")
        self.register_button.place(x=60, y=300, width=120)

        # Botón de "Login"
        self.login_button = ttk.Button(self.login_text, text="Login", command=self.login, style="LoginWindow.TButton", compound= "center")
        self.login_button.place(x=220, y=300, width=120)

    def register(self):
        # Obtener el valor de los campos de usuario y contraseña
        username = self.username_str.get()
        password = self.password_str.get()

        # Hash de la contraseña
        hashed_password = self.hash_password(password)

        # Si el nombre de usuario o la contraseña están vacíos, mostramos un mensaje de error
        if not username or not password:
            self.informant_str.set("Por favor ingrese un nombre de usuario y una contraseña")
            return

        # Conexión a la base de datos
        if self.connect_db:
            cursor = self.connect_db.cursor()  # Crear un cursor para ejecutar consultas SQL

            # Verificar si el usuario ya existe en la base de datos
            cursor.execute("SELECT * FROM USERS WHERE username = ?", (username,))
            user = cursor.fetchone()

            if user:
                self.informant_str.set("El usuario ya existe")
            else:
                # Convertir el hash de bytes a cadena antes de guardarlo
                hashed_password_str = hashed_password.decode('utf-8')
                cursor.execute("INSERT INTO USERS (username, password) VALUES (?, ?)", (username, hashed_password_str))
                self.connect_db.commit()
                self.informant_str.set("Usuario registrado exitosamente")

            cursor.close()

    def login(self):
        # Obtener el valor de los campos de usuario y contraseña
        username = self.username_str.get()
        password = self.password_str.get()

        if not username or not password:
            self.informant_str.set("Por favor ingrese un nombre de usuario y una contraseña")
            return

        if self.connect_db:
            cursor = self.connect_db.cursor()
            
            # Primero, verifica si el usuario está en la tabla de administradores
            cursor.execute("SELECT * FROM Administrators WHERE username = ?", (username,))
            admin = cursor.fetchone()
            # Si no es administrador, verificar en la tabla de usuarios
            if not admin:
                cursor.execute("SELECT * FROM USERS WHERE username = ?", (username,))
                user = cursor.fetchone()
                self.is_admin = False
                print("El usuario no es un administrador")
            else:
                user = admin
                self.is_admin = True
                print("El usuario es un administrador")

            if user:
                if admin:
                    if user[2] == password:
                        self.informant_str.set(f"¡Bienvenido {username}!")
                        self.username_callback(username)
                else:
                    stored_hash = user[2].encode('utf-8')  # Hash de la contraseña guardada
                    if self.verify_password(stored_hash, password):
                        self.informant_str.set(f"¡Bienvenido {username}!")                   
                        self.username_callback(username)
                    else:
                        self.informant_str.set("Contraseña incorrecta")
            else:
                self.informant_str.set("Usuario no encontrado. Por favor, regístrese.")

            cursor.close()


# Función para hashear la contraseña
    def hash_password(self, password):
        salt = bcrypt.gensalt()  # Genera un salt único
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password

    def verify_password(self, stored_password_hash, provided_password):   
        return bcrypt.checkpw(provided_password.encode('utf-8'), stored_password_hash)
