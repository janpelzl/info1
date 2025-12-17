from turtle import *
class Rechteck():
    def __init__(self, xpos=0, ypos=0, a=200, b=400):
        self.x = xpos
        self.y = ypos
        self.a = a
        self.b = b

    def zeichnen(self):
        penup()
        goto(self.x, self.x)
        pendown()
        forward(self.a)
        left(90)
        forward(self.b)
        left(90)
        forward(self.a)
        left(90)
        forward(self.b)

class Quadrat(Rechteck):
    def __init__(self, xpos=0, ypos=0, a=200):
        self.x = xpos
        self.y = ypos
        self.a = a
        self.b = a

# Hauptprogramm
reset()
einRechteck = Rechteck()
nochEinRechteck = Rechteck(123,180, 50, 70)
einRechteck.zeichnen()
nochEinRechteck.zeichnen()
einQuadrat = Quadrat()
einQuadrat.zeichnen()
exitonclick()
