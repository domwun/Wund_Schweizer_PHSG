
# Diese Funktion wird einmal am Anfang ausgeführt.
def setup():
    size(800, 600)  # Setze die Größe des Fensters auf 800x600 Pixel.
    frameRate(60)  # Aktualisiere 60 Mal pro Sekunde.

    # Hier zeichnen wir Quadrate für jede der RGB-Farben.
    stroke(0)  # Setze die Linienfarbe auf Schwarz.
    
    # Zeichne ein rotes Quadrat.
    fill(r_val, 0, 0)
    rect(250, 150, 200, 200)

    # Zeichne ein grünes Quadrat.
    fill(0, g_val, 0)
    rect(350, 150, 200, 200)

    # Zeichne ein blaues Quadrat.
    fill(0, 0, b_val)
    rect(300, 250, 200, 200)

    # Hier werden die Farbüberschneidungen gezeigt.
    # Rot und Grün überschneiden sich.
    fill(r_val, g_val, 0)
    rect(350, 150, 100, 200)

    # Rot und Blau überschneiden sich.
    fill(r_val, 0, b_val)
    rect(300, 250, 150, 100)

    # Grün und Blau überschneiden sich.
    fill(0, g_val, b_val)
    rect(350, 250, 150, 100)

    # Alle drei Farben überschneiden sich.
    fill(r_val, g_val, b_val)
    rect(350, 250, 100, 100)

    # Hier zeichnen wir die Schieberegler.
    draw_slider(50, 500, r_slider, 'Rot', color(255, 0, 0))
    draw_slider(300, 500, g_slider, 'Gruen', color(0, 255, 0))
    draw_slider(550, 500, b_slider, 'Blau', color(0, 0, 255))
