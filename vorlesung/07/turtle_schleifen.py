from turtle import *

reset()

for i in range(10,100,8):
    forward(i+2)
    left(90)
    forward(i+4)
    left(90)
    forward(i+6)
    left(90)
    forward(i+8)
    left(90)

exitonclick()