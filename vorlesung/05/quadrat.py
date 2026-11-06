import turtle

def quadrat(x,y,breite,strichdicke=1,farbe="black"):
    turtle.pensize(strichdicke)
    turtle.color(farbe)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.forward(breite)
    turtle.right(90)
    turtle.forward(breite)
    turtle.right(90)
    turtle.forward(breite)
    turtle.right(90)
    turtle.forward(breite)