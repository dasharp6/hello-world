import turtle
import math


def draw_koch_segment(t, run_len, mydepth, depth):
    if mydepth == depth:
        t.fd(run_len)
    else:
        temp_run = run_len/3.0
        draw_koch_segment(t, temp_run, mydepth+1, depth)
        t.left(60)
        draw_koch_segment(t, temp_run, mydepth+1, depth)
        t.right(120)
        draw_koch_segment(t, temp_run, mydepth+1, depth)
        t.left(60)
        draw_koch_segment(t, temp_run, mydepth+1, depth)
    
def main():
    wn = turtle.Screen()
    wx = 200
    wh = 200
    t_base_len = 200
    depth = 4
    koch_turtle = turtle.Turtle()
    koch_turtle.speed(50*(depth+1))
    koch_turtle.penup()
    koch_turtle.setposition((-wx/2,-wh/2))
    koch_turtle.pendown()
    koch_turtle.left(60)

    for ii in range(3):
        draw_koch_segment(koch_turtle, t_base_len, 0, depth)
        koch_turtle.right(120)
    turtle.done()
main()
