from shapes import *
import turtle
turtle.speed(0)
#colored background for the sky
nightSky = turtle.Screen()
nightSky.bgcolor('twilight')
#move to top left corner for moon
up()
left(90)
forward(192)
left(90)
forward(146)
down()
#moon
fillcolor('white')
begin_fill()
drawCircle('white', 10, 50)
end_fill()
#a bunch of stars
pencolor('yellow')
night(2, 20, 180, 5)
night(3, 10, 145, 9)
night(2, 50, 150, 5)
night(2, 139, 139, 5)
night(3, 90, 105, 9)
night(2, 120, 70, 5)
night(3, 10, 65, 9)
night(2, 34, 67, 5)
night(2, 126, 94, 5)
night(3, 130, 189, 9)
#add some landscaping
up()
left(90)
forward(300)
left(90)
forward(70)
left(180)
down()
#draw some grass
fillcolor('green')
pencolor('green')
begin_fill()
drawSquare(400, 200)
end_fill()