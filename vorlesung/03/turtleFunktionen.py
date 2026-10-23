from turtle import *
# Funktion zum Zeichnen eines Quadrates an der Stelle x,y mit der Kantenlänge b
def zeichneQuadrat(x,y,b, farbe):
    color(farbe)
    penup()
    goto(x,y)
    pendown()
    forward(b)
    left(90)
    forward(b)
    left(90)
    forward(b)
    left(90)
    forward(b)

zeichneQuadrat(200,200,10, "Red")
zeichneQuadrat(-100, 20, 50, "Blue")
zeichneQuadrat(0,50,20, "Black")
exitonclick()