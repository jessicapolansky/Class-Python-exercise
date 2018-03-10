from turtle import *

def start_draw(shape_color):
    down()
    color(shape_color, shape_color)
    begin_fill()
    
def stop_draw():
    end_fill()
    up()
    
def draw_trapezoid(sector, shape_color):
    start_draw(shape_color)
    if sector == 1:
      left(63)
      forward(94)
      right(63)
      forward(70)
      right(63)
      forward(94)
      right(117)
      forward(156)
    if sector == 2:
      right(63)
      forward(94)
      left(63)
      forward(70)
      left(63)
      forward(94)
      left(117)
      forward(156)
    stop_draw()

def draw_parallelogram(sector, shape_color):
    start_draw(shape_color)
    if sector == 1:
      forward(94)
      left(117)
      forward(94)
      left(63)
      forward(94)
      left(117)
      forward(94)
    if sector == 2:
      forward(94)
      right(117)
      forward(94)
      right(63)
      forward(94)
      right(117)
      forward(94)
    stop_draw()
    
def draw_triangle(size, shape_color, counter_rotation=False):
    start_draw(shape_color)
    if size == "small":
        side_length = 68
    elif size == "medium":
        side_length = 78
    elif size == "large":
        side_length = 94
    for i in range(0, 3):
        forward(side_length)
        if counter_rotation:
            left(120)
        else:
            right(120)
    stop_draw()