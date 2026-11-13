import turtle
import random

def rechteck(x,y,laenge):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    for i in range(4):
        turtle.forward(laenge)
        turtle.left(90)

def randomWalk1(anzahlSchritte):
    for i in range(anzahlSchritte):
        x = random.randint(-400,400)
        y = random.randint(-400,400)
        turtle.goto(x, y)

def randomWalk2(anzahlSchritte):
    for i in range(anzahlSchritte):
        schrittweite = random.randint(1,11)
        winkel = random.randint(0,180)
        turtle.forward(schrittweite)
        turtle.right(winkel)


#rechteck(10,10,100)
#rechteck(-100,-100,40)
turtle.speed(1000)
#randomWalk1(1000)
randomWalk2(2000)
turtle.exitonclick()