# Globale Variablen für die RGB-Werte und die Position der Schieberegler
r_val, g_val, b_val = 255, 255, 255  # Anfangswerte für Rot, Grün und Blau (alle auf Maximum, also Weiß).
r_slider, g_slider, b_slider = 100, 100, 100  # Anfangspositionen der Schieberegler.

# Diese Funktion wird einmal am Anfang ausgeführt.
def setup():
    size(800, 600)  # Setze die Größe des Fensters auf 800x600 Pixel.
    frameRate(60)  # Aktualisiere 60 Mal pro Sekunde.

# Diese Funktion wird immer wieder aufgerufen und zeichnet die Inhalte.
def draw():
    background(255)  # Setze den Hintergrund auf Weiß.

    # Hier wird der Titel hinzugefügt.
    fill(0)  # Setze die Füllfarbe auf Schwarz.
    textSize(32)  # Setze die Schriftgröße auf 32 Pixel.
    textAlign(CENTER, CENTER)  # Zentriere den Text horizontal und vertikal.
    text("Additive Farbmischung", width / 2, 50)  # Zeige den Titel.

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

# Diese Funktion zeichnet einen Schieberegler.
def draw_slider(x, y, position, label, col):
    # Zeichne die Linie des Schiebreglers.
    stroke(0)
    line(x, y, x + 200, y)
    # Zeichne den Schieberegler-Knopf.
    fill(col)
    ellipse(x + position, y, 20, 20)
    # Zeige das Label des Schiebreglers.
    fill(0)
    text(label, x + 90, y - 40)

# Diese Funktion wird aufgerufen, wenn die Maus gezogen wird.
def mouseDragged():
    global r_slider, g_slider, b_slider  # Wir arbeiten mit globalen Variablen.
    global r_val, g_val, b_val

    # Wenn die Maus in der Nähe der Schieberegler ist.
    if 480 < mouseY < 520:
        # Überprüfen, über welchem Schieberegler sich die Maus befindet und ändern Sie die Position/Werte.
        if 50 <= mouseX <= 250:
            r_slider = constrain(mouseX - 50, 0, 200)
            r_val = map(r_slider, 0, 200, 0, 255)
        elif 300 <= mouseX <= 500:
            g_slider = constrain(mouseX - 300, 0, 200)
            g_val = map(g_slider, 0, 200, 0, 255)
        elif 550 <= mouseX <= 750:
            b_slider = constrain(mouseX - 550, 0, 200)
            b_val = map(b_slider, 0, 200, 0, 255)
