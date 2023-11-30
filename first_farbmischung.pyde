# Definieren Sie die anfänglichen RGB-Werte
red_value = 0
green_value = 0
blue_value = 0

# Position und Größe der Schieberegler
slider_x = 50
slider_y = 50
slider_width = 200
slider_height = 20
gap = 30  # Abstand zwischen den Schiebereglern

# Um zu überprüfen, ob ein Schieberegler gerade gezogen wird
dragging_red = False
dragging_green = False
dragging_blue = False

def setup():
    size(400, 400)
    background(255)

def draw():
    background(255)
    
    # Schieberegler zeichnen
    draw_slider(slider_x, slider_y, red_value, color(255, 0, 0))
    draw_slider(slider_x, slider_y + gap, green_value, color(0, 255, 0))
    draw_slider(slider_x, slider_y + 2*gap, blue_value, color(0, 0, 255))

    # Additive Farbmischung anzeigen
    fill(red_value, green_value, blue_value)
    rect(300, 50, 50, 50)

def draw_slider(x, y, value, col):
    # Schieberegler-Hintergrund
    fill(200)
    rect(x, y, slider_width, slider_height)
    # Schieberegler-Position
    fill(col)
    rect(x + value - 5, y, 10, slider_height)

def mousePressed():
    global dragging_red, dragging_green, dragging_blue
    
    if slider_x <= mouseX <= slider_x + slider_width:
        if slider_y <= mouseY <= slider_y + slider_height:
            dragging_red = True
        elif slider_y + gap <= mouseY <= slider_y + gap + slider_height:
            dragging_green = True
        elif slider_y + 2*gap <= mouseY <= slider_y + 2*gap + slider_height:
            dragging_blue = True

def mouseReleased():
    global dragging_red, dragging_green, dragging_blue
    dragging_red = False
    dragging_green = False
    dragging_blue = False

def mouseDragged():
    global red_value, green_value, blue_value
    
    if dragging_red:
        red_value = constrain(mouseX - slider_x, 0, slider_width)
    elif dragging_green:
        green_value = constrain(mouseX - slider_x, 0, slider_width)
    elif dragging_blue:
        blue_value = constrain(mouseX - slider_x, 0, slider_width)
    elif dragging_green:
        green_value = constrain(mouseX - slider_x, 0, slider_width)
    elif dragging_blue:
        blue_value = constrain(mouseX - slider_x, 0, slider_width)
