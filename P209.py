def drawSquare(t, x, y, length):
    t.up()
    t.goto(x, y)
    t.setheading(270)
    t.down()
    for count in range(4):
        t.forward(length)
        t.left(90)
        
from polygons import *
from turtle import Turtle

t = Turtle()
t.pencolor("blue")
t.hideturtle()
square(t, 50)
