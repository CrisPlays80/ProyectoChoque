import tkinter as tk
from tkinter import ttk
from datetime import datetime

class AlertTimeline(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#252330")
        self.create_timeline()
        self.pack(expand=True, fill="both")

    def create_timeline(self):
        # Título
        title = tk.Label(self, text="Alertas", font=("CreatoDisplay-Regular", 16), bg="#252330", fg="white")
        title.pack(pady=10)

        # Scrollable frame para el timeline
        container = tk.Frame(self, bg="#252330")
        canvas = tk.Canvas(container, bg="#252330", highlightthickness=0)
        scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        container.pack(fill="both", expand=True)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Crear alertas como eventos en el timeline
        self.alerts = [
            {"time": datetime.now().strftime("%Y-%m-%d %H:%M"), "icon": "⚠️", "text": "Error en la conexión", "details": "Hubo un problema al conectar con el servidor."},
            {"time": datetime.now().strftime("%Y-%m-%d %H:%M"), "icon": "✅", "text": "Actualización completada", "details": "El sistema se actualizó correctamente."},
            {"time": datetime.now().strftime("%Y-%m-%d %H:%M"), "icon": "🔔", "text": "Nuevo mensaje", "details": "Tienes un nuevo mensaje en tu bandeja de entrada."},
        ]

        for alert in self.alerts:
            self.add_alert_event(scrollable_frame, alert)

    def add_alert_event(self, parent, alert):
        """
        Añadir un evento de alerta al timeline.
        """
        frame = ttk.Frame(parent)
        frame.pack(fill="x", pady=10, padx=10, anchor="w")

        # Icono de alerta
        icon_label = tk.Label(frame, text=alert["icon"], font=("CreatoDisplay-Regular", 24), bg="#252330", fg="white")
        icon_label.grid(row=0, column=0, padx=10)

        # Descripción de alerta
        text_frame = ttk.Frame(frame)
        text_frame.grid(row=0, column=1, sticky="w")

        # Hora y mensaje principal
        time_label = tk.Label(text_frame, text=alert["time"], font=("CreatoDisplay-Regular", 10), bg="#252330", fg="white")
        time_label.pack(anchor="w")
        text_label = tk.Label(text_frame, text=alert["text"], font=("CreatoDisplay-Regular", 12, "bold"), bg="#252330", fg="white")
        text_label.pack(anchor="w")

        # Botón para expandir detalles
        details_button = tk.Button(text_frame, text="Ver detalles", font=("CreatoDisplay-Regular", 10), bg="#252330", fg="white", command=lambda: self.show_details(alert["details"]))
        details_button.pack(anchor="w", pady=2)

    def show_details(self, details):
        """
        Mostrar una ventana emergente con los detalles de la alerta.
        """
        details_window = tk.Toplevel(self)
        details_window.title("Detalles de la Alerta")
        details_window.geometry("300x150")
        details_window.configure(bg="#252330")

        details_label = tk.Label(details_window, text=details, wraplength=280, bg="#252330", fg="white", font=("CreatoDisplay-Regular", 12))
        details_label.pack(pady=20, padx=20)