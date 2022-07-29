def radialHexagons(t, n, length):
	for count in range(n):
		hexagon(t, length)
		t.left(360 / n)

from polygons import *
from turtle import Turtle

t = Turtle()
t.pencolor("blue")
t.hideturtle()
square(t, 50)
hexagon(t, 50)
t.clear()
radialHexagons(t, 10, 50)
