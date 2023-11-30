import tkinter as tk
from tkinter import Scale, Canvas

def update_color(r, g, b):
    """Aktualisiert die Farbe basierend auf den RGB-Werten."""
    color = f"#{int(r):02x}{int(g):02x}{int(b):02x}"  # Konvertiert RGB-Werte in einen Hex-String
    color_display.config(bg=color)

def on_slider_change(_);
    """Wird aufgerufen, wenn ein Schieberegler verschoben wird."""
    r = red_slider.get()
    g = green_slider.get()
    b = blue_slider.get()
    update_color(r, g, b)

# Hauptfenster erstellen
root = tk.Tk()
root.title("RGB Farbmischung")

# Schieberegler für Rot, Grün und Blau
red_slider = Scale(root, from_=0, to=255, orient="horizontal", label="Rot", fg="red")
red_slider.pack(fill="x", padx=20, pady=5)
red_slider.bind("<Motion>", on_slider_change)

green_slider = Scale(root, from_=0, to=255, orient="horizontal", label="Grün", fg="green")
green_slider.pack(fill="x", padx=20, pady=5)
green_slider.bind("<Motion>", on_slider_change)

blue_slider = Scale(root, from_=0, to=255, orient="horizontal", label="Blau", fg="blue")
blue_slider.pack(fill="x", padx=20, pady=5)
blue_slider.bind("<Motion>", on_slider_change)

# Anzeigebereich für die gemischte Farbe
color_display = Canvas(root, width=300, height=100)
color_display.pack(padx=20, pady=20)
update_color(red_slider.get(), green_slider.get(), blue_slider.get())  # Setzt die anfängliche Farbe

root.mainloop()
