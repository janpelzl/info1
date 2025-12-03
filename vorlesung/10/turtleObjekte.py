import turtle
import random

t1 = turtle.Turtle()
t2 = turtle.Turtle()

t1.speed(500)
t1.color("red")

for i in range(500):
    t1.left(random.randint(0,360))
    t2.left(random.randint(0,360))
    t1.forward(random.randint(0,20))
    t2.forward(random.randint(0,20))



turtle.exitonclick()
