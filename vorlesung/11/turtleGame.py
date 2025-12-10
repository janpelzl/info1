import turtle
import random

punkte = 0

# Methoden zur Richtungsänderung
def nachOben():
    player.setheading(90)
def nachUnten():
    player.setheading(270)
def nachRechts():
    player.setheading(0)
def nachLinks():
    player.setheading(180)

player = turtle.Turtle()
player.penup()
player.color("white")
player.shape("turtle")

futter = turtle.Turtle()
futter.color("blue")
futter.shape("circle")
futter.penup()

anzeige = turtle.Turtle()
anzeige.penup()
anzeige.color("white")
anzeige.hideturtle()
anzeige.goto(-20,300)
anzeige.write(f"Punkte: {punkte}", align="center", font=("candara", 24, "bold"))

screen = turtle.Screen()
screen.bgcolor("black")
screen.listen()
screen.screensize(800,800)
screen.onkeypress(nachOben,"Up")
screen.onkeypress(nachUnten,"Down")
screen.onkeypress(nachLinks,"Left")
screen.onkeypress(nachRechts,"Right")

#  Hauptprogramm
while True:
    player.forward(1)
    if player.distance(futter) < 10:
        punkte = punkte + 1
        print(punkte)
        futter.goto( random.randint(-200,200), random.randint(-200,200))
    screen.update()