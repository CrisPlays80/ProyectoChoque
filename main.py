import tkinter as tk
from windows import LoginWindow
from frame import Dashboard, Header


class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Main Application")
        self.configure(bg="#252330")
        self.state("zoomed")

        self.content_frame = tk.Frame(self, bg="#ffffff")
        
        self.dashboard = Dashboard(self, self.content_frame)
        self.dashboard.pack(side="left", fill="y")
        
        self.header_frame = Header(self)
        self.header_frame.pack(side="top", fill="x")
        
        self.content_frame.pack(expand=True, fill="both")
        self.content_frame.pack_propagate(False)

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()