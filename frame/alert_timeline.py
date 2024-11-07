import tkinter as tk
from tkinter import ttk
from datetime import datetime
import random

class AlertTimeline(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#252330")
        self.create_timeline()
        self.pack(expand=True, fill="both")

    def create_timeline(self):
        # Título
        self.add_title()

        # Frame contenedor para el canvas y la scrollbar
        container = tk.Frame(self, bg="#252330")
        container.pack(fill="both", expand=True, padx=20, pady=10)

        # Canvas para el contenido del timeline
        canvas = tk.Canvas(container, bg="#252330", highlightthickness=0)
        canvas.pack(side="left", fill="both", expand=True)

        # Scrollbar vertical
        scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")
        canvas.configure(yscrollcommand=scrollbar.set)

        # Frame para los eventos de alerta
        scrollable_frame = ttk.Frame(canvas)
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        # Lista de alertas
        self.alerts = self.generate_alerts()

        # Añadir alertas
        for alert in self.alerts:
            self.add_alert_event(scrollable_frame, alert)

    def add_title(self):
        """Añadir título al panel de alertas"""
        title = tk.Label(self, text="Alertas", font=("CreatoDisplay-Regular", 16), bg="#252330", fg="white")
        title.pack(pady=10)

    def generate_alerts(self):
        """Generar una lista de alertas simuladas"""
        base_alerts = [
            {"icon": "⚠️", "text": "Error en la conexión", "details": "Hubo un problema al conectar con el servidor."},
            {"icon": "✅", "text": "Actualización completada", "details": "El sistema se actualizó correctamente."},
            {"icon": "🔔", "text": "Nuevo mensaje", "details": "Tienes un nuevo mensaje en tu bandeja de entrada."},
            {"icon": "🚨", "text": "Alerta de seguridad", "details": "Se detectó un intento de acceso no autorizado."},
            {"icon": "💾", "text": "Copia de seguridad completada", "details": "La copia de seguridad se realizó sin problemas."},
        ]

        alerts = []
        for _ in range(23):  # Crear 23 alertas aleatorias
            alert = random.choice(base_alerts)
            alert_copy = alert.copy()
            alert_copy["time"] = datetime.now().strftime("%Y-%m-%d %H:%M")
            alerts.append(alert_copy)

        return alerts

    def add_alert_event(self, parent, alert):
        """Añadir un evento de alerta al timeline"""
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
        """Mostrar una ventana emergente con los detalles de la alerta"""
        details_window = tk.Toplevel(self)
        details_window.title("Detalles de la Alerta")
        details_window.geometry("300x150")
        details_window.configure(bg="#252330")

        details_label = tk.Label(details_window, text=details, wraplength=280, bg="#252330", fg="white", font=("CreatoDisplay-Regular", 12))
        details_label.pack(pady=20, padx=20)