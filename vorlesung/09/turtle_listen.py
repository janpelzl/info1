import turtle
import random

liste = []
for i in range(5):
    liste.append( turtle.Turtle() )

turtle.reset()

for i in liste:
    i.left( random.randint(0,360) )
    i.forward(random.randint(0,200))

turtle.exitonclick()