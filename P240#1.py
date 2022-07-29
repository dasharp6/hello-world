"""
File: drawCircle.py"""

import turtle
import math

def drawCircle(turtleobj, x, y, radius):
     distance = 2 * radius * math.sin (math.pi / 120)
     angle = 360 / 120
     turtleobj.penup()
     turtleobj.goto (x, y)
     turtleobj.pendown()
     for iter in range (120):
         turtleobj.forward(distance)
         turtleobj.left(angle)

def main():
    X=int(input("Enter X : "));
    Y=int(input("Enter Y : "));
    radius=int(input("Enter Radius : "));
    turtle.title ('Circle')
    turtle.setup (800, 800, 0, 0)
    ttl = turtle.Turtle()
    ttl.color ('Blue')
    drawCircle (ttl,X, Y,radius)
    turtle.done()
main()
