import tkinter as tk
from tkinter import ttk

class RoundedFrame(tk.Canvas):
    def __init__(self, parent, width, height, corner_radius, color):
        super().__init__(parent, width=width, height=height, bg=parent['bg'], highlightthickness=0)
        self.corner_radius = corner_radius
        self.color = color

        # Crear el fondo redondeado
        self.create_rounded_rect(0, 0, width, height, corner_radius, color)

    def create_rounded_rect(self, x1, y1, x2, y2, r, color):
        """Dibuja un rectángulo redondeado en el canvas"""
        points = [
            x1 + r, y1,  # punto inicial
            x1 + r, y1,  # arco superior izquierdo
            x2 - r, y1,
            x2 - r, y1,
            x2, y1,
            x2, y1 + r,
            x2, y1 + r,
            x2, y2 - r,
            x2, y2 - r,
            x2, y2,
            x2 - r, y2,
            x2 - r, y2,
            x1 + r, y2,
            x1 + r, y2,
            x1, y2,
            x1, y2 - r,
            x1, y2 - r,
            x1, y1 + r,
            x1, y1 + r,
            x1, y1
        ]
        self.create_polygon(points, fill=color, smooth=True, outline=color)