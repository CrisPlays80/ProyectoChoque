import tkinter as tk
import ttkbootstrap as ttk

window_main = ttk.Window()
window_main.title("GPS")
window_main.attributes("-fullscreen", True)


header_frame = ttk.Frame(window_main, height=50,style="primary")
header_frame.pack(side=tk.TOP, fill=tk.X)

style = ttk.Style()

# Dashboard
dashboard_frame = ttk.Frame(window_main, width = 50, style="success")
dashboard_frame.pack(side=tk.LEFT, fill=tk.Y)

# Main Content
content_frame = ttk.Frame(window_main, style="light")
content_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

def close_window(event):
    window_main.destroy()

window_main.bind("<Escape>", close_window)
window_main.mainloop()