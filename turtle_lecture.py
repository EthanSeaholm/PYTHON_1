#

import turtle

s=turtle.getscreen()
t=turtle.Turtle()

#t.goto(20,20)
#t.circle(100)

#t.dot(120)

turtle.bgcolor("gray")

#t.shapesize(15,5,1)
#t.fillcolor("red") # fills the inside of the shape
#t.color("green","red") # outlines the shape w/ first color/changes movement's line color, fills w/ second color
#t.fd(100) # moves the shape from the center and draws a line showing its movement
#t.pensize(1) # changes the movement's line size
#t.pencolor("pink") # changes the shape's outline color and overrides t.color's outline color, but not t.color's fill or movement color

#t.shape("turtle ")
#can use circle, square, arrow, turtle, triangle, classic

#t.begin_fill()
#t.fd(100)
#t.lt(120)
#t.fd(100)
#t.lt(120)
#t.fd(100)
#t.end_fill()

t.pen(pencolor = "purple", fillcolor = "yellow", pensize = 10, speed = 5)
t.begin_fill()
t.circle(100)
t.end_fill()

#