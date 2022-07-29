from polygons import *
from turtle import Turtle

def radialPattern(t, n, length, shape):
    for count in range(n):
        shape(t, length)
        t.left(360 / n)

t = Turtle()
t.pencolor("red")
radialPattern(t, n = 10, length = 50, shape = square)
t.clear()
t.pencolor("blue")
radialPattern(t, n = 10, length = 50, shape = hexagon)
