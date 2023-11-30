# Globale Variablen für die RGB-Werte 
r_val, g_val, b_val = 255, 255, 255  # Anfangswerte für Rot, Grün und Blau (alle auf Maximum, das gibt also Weiss).
r_slider, g_slider, b_slider = 100, 100, 100  # Anfangspositionen der Schieberegler.

def setup():
    size(800, 600)  # Setze die Größe des Fensters auf 800x600 Pixel.
    frameRate(60)  # Aktualisiere 60 Mal pro Sekunde.


    # Hier wird der Titel hinzugefügt.
    fill(0)  # Setze die Füllfarbe auf Schwarz.
    textSize(32)  # Setze die Schriftgröße auf 32 Pixel.
    textAlign(CENTER, CENTER)  # Zentriere den Text horizontal und vertikal.
    text("Additive Farbmischung", width / 2, 50)  # Zeige den Titel.

    # Hier zeichnen wir Quadrate für jede der RGB-Farben.
    stroke(0)  # Setze die Linienfarbe auf Schwarz.
    
    #  ein rotes Quadrat.
    fill(r_val, 0, 0)
    rect(250, 150, 200, 200)

    # ein grünes Quadrat.
    fill(0, g_val, 0)
    rect(350, 150, 200, 200)

    # ein blaues Quadrat.
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
