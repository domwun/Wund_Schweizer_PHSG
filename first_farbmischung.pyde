     #Importieren der ControlP5 Bibliothek
import controlP5.*;

ControlP5 cp5;

    #Initialwerte für die Slider Cyan, Magenta, Gelb
int cyan = 0;
int magenta = 0;
int yellow = 0;

void setup() {
  size(600, 400);
  background(255);
  
  #Erstellen der ControlP5-Instanz
  cp5 = new ControlP5(this);

  #Erstellen der Schieberegler für Cyan, Magenta und Gelb
  cp5.addSlider("cyan")
     .setPosition(50, 50)
     .setSize(200, 20)
     .setRange(0, 255)
     .setValue(0)
     .setLabel("Cyan");
     
  cp5.addSlider("magenta")
     .setPosition(50, 100)
     .setSize(200, 20)
     .setRange(0, 255)
     .setValue(0)
     .setLabel("Magenta");
     
  cp5.addSlider("yellow")
     .setPosition(50, 150)
     .setSize(200, 20)
     .setRange(0, 255)
     .setValue(0)
     .setLabel("Gelb");
}

void draw() {
  background(255);
  
  #Subtraktive Farbmischung
 #Wir beginnen mit Weiß und ziehen dann die RGB-Werte ab, die den CMY-Werten entsprechen
  int r = 255 - cyan;
  int g = 255 - magenta;
  int b = 255 - yellow;

  #Setzen der subtraktiven Farbe als Hintergrund
  fill(r, g, b);
  rect(300, 50, 200, 200);
}

#Diese Funktionen werden aufgerufen, wenn die Schieberegler bewegt werden
void cyan(int value) {
  cyan = value;
}

void magenta(int value) {
  magenta = value;
}

void yellow(int value) {
  yellow = value;
}
