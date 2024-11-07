from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk
from tkinter import ttk

class Graph(tk.Frame):
    def __init__(self, parent, velocidad, orientacion, triage):
        super().__init__(parent, bg="#252330")  # Fondo oscuro para el dashboard
        self.velocidad = velocidad
        self.orientacion = orientacion
        self.triage = triage

        self.create_dashboard()  # Crea el dashboard de gráficos
        self.pack(expand=True, fill="both")

    def create_dashboard(self):
        """
        Crear un dashboard con múltiples gráficos.
        """
        self.fig = Figure(figsize=(12, 5), dpi=100)
        self.fig.patch.set_facecolor("#252330")  # Cambiar fondo de la figura

        # Colores personalizados para los gráficos
        color_velocidad = '#ff7f50'  # Color coral para Velocidad
        color_triage = '#1e90ff'     # Color azul para Triage

        # Gráfico 1: Velocidad vs Triage
        ax1 = self.fig.add_subplot(221)
        ax1.scatter(self.velocidad, self.triage, color=color_triage, s=20, label="Triage")
        ax1.set_title("Velocidad vs Triage", color="white", fontsize=12)
        ax1.set_xlabel("Velocidad", color="white", fontsize=10)
        ax1.set_ylabel("Triage", color="white", fontsize=10)
        ax1.legend()
        ax1.set_facecolor("#3b384d")
        ax1.tick_params(axis='x', colors='white')
        ax1.tick_params(axis='y', colors='white')

        # Gráfico 2: Orientación vs Velocidad
        ax2 = self.fig.add_subplot(222)
        ax2.scatter(self.orientacion, self.velocidad, color=color_velocidad, s=20, label="Velocidad")
        ax2.set_title("Orientación vs Velocidad", color="white", fontsize=12)
        ax2.set_xlabel("Orientación", color="white", fontsize=10)
        ax2.set_ylabel("Velocidad", color="white", fontsize=10)
        ax2.legend()
        ax2.set_facecolor("#3b384d")
        ax2.tick_params(axis='x', colors='white')
        ax2.tick_params(axis='y', colors='white')

        # Gráfico 3: Histograma de Triage
        ax3 = self.fig.add_subplot(223)
        ax3.hist(self.triage, bins=5, color=color_triage, alpha=0.7, rwidth=0.85)
        ax3.set_title("Histograma de Triage", color="white", fontsize=12)
        ax3.set_xlabel("Triage", color="white", fontsize=10)
        ax3.set_ylabel("Frecuencia", color="white", fontsize=10)
        ax3.set_xlim(1, 5)
        ax3.set_xticks([1, 2, 3, 4, 5])
        ax3.set_facecolor("#3b384d")
        ax3.tick_params(axis='x', colors='white')
        ax3.tick_params(axis='y', colors='white')

        # Gráfico 4: Gráfica de pastel de Triage
        ax4 = self.fig.add_subplot(224)
        triage_counts = {i: self.triage.count(i) for i in set(self.triage)}
        labels = [f'Triage {k}' for k in triage_counts.keys()]
        sizes = triage_counts.values()
        colors = ['#d11326', '#e57614', '#e5e514', '#0a9113', '#28c5e0']
        wedges , text = ax4.pie(sizes, colors=colors, startangle=90, wedgeprops=dict(edgecolor='white'))
        ax4.legend(wedges, [f'{label}: {size/sum(sizes) * 100:.1f}%' for label, size in zip(labels, sizes)], 
        title="Distribución de Triage", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
        ax4.set_title('Distribución de Triage', color="white", fontsize=12)
        ax4.set_facecolor("#3b384d")

        # Ajustar los márgenes entre los gráficos
        self.fig.tight_layout(pad=3.0)
        self.fig.subplots_adjust(top=0.9, bottom=0.1, hspace=0.4, wspace=0.4)

        # Crear canvas para mostrar los gráficos
        self.canvas = FigureCanvasTkAgg(self.fig, self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(expand=True, fill="both")