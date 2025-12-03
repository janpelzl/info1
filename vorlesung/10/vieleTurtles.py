import turtle
import random


meineKroeten = []
farben = ["black", "red", "blue", "yellow", "purple", "green", "brown"]
turtle.speed(1000)

for i in range(10):
    kroete = turtle.Turtle()
    kroete.pensize(random.randint(1,5))
    kroete.penup()
    kroete.goto(random.randint(-400, 400), random.randint(-400, 400))
    kroete.pendown()
    kroete.color( random.choice( farben ) )
    meineKroeten.append(kroete)

for iterationen in range(200):
    for kroete in meineKroeten:
        kroete.left(random.randint(0, 360))
        kroete.forward(random.randint(0,30))

turtle.exitonclick()