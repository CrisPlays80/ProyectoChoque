import tkinter as tk
from assets.colors.colors import AppStyle
from windows import LoginWindow
from frame import Dashboard, Header
from app.connect_db import connect_db

class MainApp(tk.Tk):
    def __init__(self, connect_db):
        super().__init__()
        self.title("Main Application")
        self.configure(bg="#252330")
        self.state("zoomed")
        self.db_connection = connect_db
        self.is_admin = False
        
        self.style = AppStyle()

        self.logged_in = False
        self.username = None

        self.show_login()
            

    def show_login(self):
        self.login_window = LoginWindow(self, self.db_connection, self.login_success, self.style)
        self.login_window.pack()

    def login_success(self, username):
        self.logged_in = True
        self.username = username
        self.is_admin = self.login_window.is_admin
        self.login_window.destroy()

        self.show_main_content()

    def show_main_content(self):
        self.content_frame = tk.Frame(self, bg="#252330")
            
        self.dashboard = Dashboard(self, self.content_frame, self.db_connection, self.logout, self.is_admin, self.style)
        self.dashboard.pack(side="left", fill="y")
                
        self.header_frame = Header(self, self.db_connection, self.style)
        self.header_frame.pack(side="top", fill="x")
                
        self.content_frame.pack(expand=True, fill="both")
        self.content_frame.pack_propagate(False)

    def logout(self):
        # Función de logout
        self.logged_in = False
        self.username = None
        self.dashboard.destroy()
        self.content_frame.destroy()  # Destruir el contenido actual
        self.header_frame.destroy()   # Destruir el header
        self.show_login() 

if __name__ == "__main__":
    connect_db = connect_db()
    app = MainApp(connect_db)
    app.mainloop()
    if connect_db:
        connect_db.close()