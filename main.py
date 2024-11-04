import tkinter as tk
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

        self.logged_in = False
        self.username = None

        self.show_login()
            

    def show_login(self):
        self.login_window = LoginWindow(self, self.db_connection, self.login_success)
        self.login_window.pack()

    def login_success(self, username):
        self.logged_in = True
        self.username = username
        self.login_window.destroy()

        self.show_main_content()

    def show_main_content(self):
        self.content_frame = tk.Frame(self, bg="#252330")
            
        self.dashboard = Dashboard(self, self.content_frame, self.db_connection)
        self.dashboard.pack(side="left", fill="y")
                
        self.header_frame = Header(self, self.db_connection)
        self.header_frame.pack(side="top", fill="x")
                
        self.content_frame.pack(expand=True, fill="both")
        self.content_frame.pack_propagate(False)

if __name__ == "__main__":
    connect_db = connect_db()
    app = MainApp(connect_db)
    app.mainloop()
    if connect_db:
        connect_db.close()