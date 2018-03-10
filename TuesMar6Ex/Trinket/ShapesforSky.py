from turtle import *

#Nighttime drawing
def night(thick, x, y, size):
  width(thick)
  up()
  goto(x,y)
  down()
  drawStar(size)
  
#circle
def drawCircle(colory, wholey, bigly):
  pencolor(colory)
  width(wholey)
  circle(bigly)

#star
def drawStar(size):
  for i in range(5):
    forward(size)
    right(144)
    
#octagon
def drawOctagon():
  forward(80)
  left(45)
  forward(80)
  left(45)
  forward(80)
  left(45)
  forward(80)
  left(45)
  forward(80)
  left(45)
  forward(80)
  left(45)
  forward(80)
  left(45)
  forward(80)

#hexagon
def drawHex():
  forward(100)
  left(60)
  forward(100)
  left(60)
  forward(100)
  left(60)
  forward(100)
  left(60)
  forward(100)
  left(60)
  forward(100)

#pentagon
def drawPenta():
  forward(100)
  left(72)
  forward(100)
  left(72)
  forward(100)
  left(72)
  forward(100)
  left(72)
  forward(100)

#square
def drawSquare(x,y):
  pencolor
  forward(x)
  left(90)
  forward(y)
  left(90)
  forward(x)
  left(90)
  forward(y)

#triangle
def drawTriangle():
  forward(100)
  left(120)
  forward(100)
  left(120)
  forward(100)