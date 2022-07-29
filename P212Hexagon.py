def hexagon(t, length):
    for count in range(6):
        t.forward(length)
        t.left(60)

from polygons import *
from turtle import Turtle

t = Turtle()
t.pencolor("blue")
t.hideturtle()
hexagon(t, 50)
