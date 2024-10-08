import tkinter as tk
from windows import LoginWindow
from frame import Dashboard

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Main Application")
        self.configure(bg="#252330")
        self.state("zoomed")
        #  Guardamos el largo y alto de la ventana
        """ wventana = 1280
        hventana = 540
        #  Aplicamos la siguiente formula para calcular donde debería posicionarse
        pwidth = round(wtotal/2-wventana/2)
        pheight = round(htotal/2-hventana/2)
        #  Se lo aplicamos a la geometría de la ventana
        self.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight)) """
        self.dashboard = Dashboard(self)
        self.dashboard.pack(side="left", fill="y", expand=True)

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()