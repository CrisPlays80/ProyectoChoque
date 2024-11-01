import pyodbc
import tkinter as tk
from tkinter import messagebox

# Función para conectar a la base de datos
def connect_db():
    server = 'sqlchoque.database.windows.net'
    database = 'sqlChoque'
    username = 'admin1234'
    password = 'sqlserver1234@'
    driver = '{ODBC Driver 17 for SQL Server}'
    try:
        connection = pyodbc.connect(f'DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database};UID={username};PWD={password}')
        return connection
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo conectar a la base de datos: {e}")
        return None
