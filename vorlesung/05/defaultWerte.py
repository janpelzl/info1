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

quadrat(0,0,30,4,"blue")
quadrat(100,100,100)
quadrat(-200,100,50)
quadrat(-100,100,20)
turtle.exitonclick()
