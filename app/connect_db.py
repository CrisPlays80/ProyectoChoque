import os
import pyodbc
import tkinter as tk
from tkinter import messagebox
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Function to connect to the database
def connect_db():
    server = os.environ.get('DB_SERVER')
    database = os.environ.get('DB_NAME')
    username = os.environ.get('DB_USERNAME')
    password = os.environ.get('DB_PASSWORD')
    driver = '{ODBC Driver 17 for SQL Server}'
    
    try:
        connection = pyodbc.connect(f'DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database};UID={username};PWD={password}')
        return connection
    except Exception as e:
        messagebox.showerror("Error", f"Failed to connect to the database: {e}")
        return None