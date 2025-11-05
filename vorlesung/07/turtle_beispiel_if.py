# Beispiel einer bedingten Anweisung mit der Turtle
from turtle import *
from random import *

reset()
speed(100)

for i in range(500):
    forward( randint(1,100))
    left( randint(0,360))
    position = pos()
    # überprüfe, ob der x-wert (Index 0) und der y-wert (Index) der turtle im gültigen Bereich
    if position[0] > 200 or position[0] < -200 or position[1] > 200 or position[1] < -200:
        goto(0,0)
        print("Turtle zurückgesetzt")

exitonclick()
