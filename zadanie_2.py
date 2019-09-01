from drawman import *
from time import sleep

def f(x):
    return x*x

def draw_grid(x_min, y_min):
    for i in range(10*2+1):
        pen_up()
        to_point(x_min + i, y_min)
        pen_down()
        on_vector(0,20)
    pen_up()
    for i in range(10*2+1):
        pen_up()
        to_point(x_min, y_min + i)
        pen_down()
        on_vector(20,0)
    pen_up()

drawman_scale(30)
draw_grid(-10,-10)

x = -5.0
to_point(x, f(x))
pen_down()
while x < 5:
    to_point(x,f(x))
    x += 0.1

pen_up()
sleep(3)

