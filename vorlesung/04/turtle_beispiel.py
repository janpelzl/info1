from turtle import *

def quadrat(kantenlaenge,x,y, dicke, farbe):
    pensize(dicke)
    color(farbe)
    penup()
    goto(x, y)
    pendown()
    forward(kantenlaenge)
    left(90)
    forward(kantenlaenge)
    left(90)
    forward(kantenlaenge)
    left(90)
    forward(kantenlaenge)

reset()

quadrat(100,0,0, 1, "black")
quadrat(30,200,20, 3, "green")
quadrat(130,-100,-120, 10, "red")

exitonclick()