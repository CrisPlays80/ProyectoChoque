import pymssql
import tkinter as tk
from tkinter import messagebox

# Función para conectar a la base de datos
def connect_db():
    try:
        connection = pymssql.connect(    
            server='sqlchoque.database.windows.net', user='admin1234', password='sqlserver1234@', database='sqlChoque'
        )
        return connection
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo conectar a la base de datos: {e}")
        return None
