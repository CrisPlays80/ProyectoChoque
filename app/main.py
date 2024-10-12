import tkinter as tk
from windows import LoginWindow
from frame import Dashboard

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Main Application")
        self.configure(bg="#252330")
        self.state("zoomed")
        self.dashboard = Dashboard(self, self)
        self.dashboard.pack(side="left", fill="y")

        self.content_frame = tk.Frame(self, bg="#252330")
        self.content_frame.pack(side="right", fill="both", expand=True)

        self.label = tk.Label(self.content_frame, text="Contentososoosososo", bg="#252330", fg="white")
        self.label.pack(side="top", fill="both", expand=True)


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()