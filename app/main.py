import tkinter as tk
from windows import LoginWindow
from frame import Header

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Main Application")
        self.geometry("1280x720")

        self.header = Header(self)
        self.header.pack(side = "top", fill="x")
        
        self.dashboard = tk.Frame(self, background="#0b5563", width=60)
        self.dashboard.pack(side="left", fill="y")        
        
        # Button to open login window
        self.open_login_button = tk.Button(self, text="Open Login Window", command=self.open_login_window)
        self.open_login_button.pack(pady=20)

    def open_login_window(self):
        # Open the LoginWindow
        login_window = LoginWindow(self)

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()