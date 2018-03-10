from shapes import *
from turtle import *

if __name__ == "__main__":
    Screen().setup(800,800)
    up()
    hideturtle()
    pensize(.1)
    speed("fast")
  
    goto(-350, 250)
    setheading(0)
    draw_trapezoid(1, "#7CC242")
    
    setheading(0)
    forward(156)
    draw_parallelogram(1, "#5B893D")
    
    setheading(0)
    draw_triangle("small", "#8EC63F")
    
    left(120)
    backward(68)
    setheading(0)
    draw_triangle("large", "#447865", True)
    
    right(120)
    backward(94)
    setheading(0)
    draw_triangle("large", "#1483B3")
    
    setheading(0)
    forward(94)
    right(60)
    draw_triangle("medium", "#1F8DCD")
    
    goto(-350, 132.2205)
    setheading(0)
    draw_trapezoid(2, "#1F8DCD")
    
    setheading(0)
    forward(156)
    draw_parallelogram(2, "#0C6FB8")
    
    setheading(0)
    draw_triangle("small", "#2093D1", True)
    
    right(120)
    backward(68)
    setheading(0)
    draw_triangle("large", "#1466A3")
    
    goto(309, 132.2205)
    setheading(180)
    draw_trapezoid(1, "#F99F1F")
    
    setheading(180)
    forward(156)
    draw_parallelogram(1, "#F47820")
    
    setheading(180)
    draw_triangle("small", "#FCB315")
    
    left(120)
    backward(68)
    setheading(180)
    draw_triangle("large", "#C28254", True)
    
    right(120)
    backward(94)
    setheading(180)
    draw_triangle("large", "#6E6E71")
    
    setheading(180)
    forward(94)
    right(60)
    draw_triangle("medium", "#A6AAAB")
    
    goto(309, 250)
    setheading(180)
    draw_trapezoid(2, "#BBBDBF")
    
    setheading(180)
    forward(156)
    draw_parallelogram(2, "#A6AAAB")
    
    setheading(180)
    draw_triangle("small", "#BBBDBF", True)
    
    right(120)
    backward(68)
    setheading(180)
    draw_triangle("large", "#939597")
