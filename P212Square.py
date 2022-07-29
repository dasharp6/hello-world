def square(t, length):
    for count in range(4):
        t.forward(length)
        t.left(90)
        
from polygons import *
from turtle import Turtle

t = Turtle()
t.pencolor("blue")
t.hideturtle()
square(t, 50)

