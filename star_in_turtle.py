#

import turtle
 
screen = turtle.getscreen()
t = turtle.Turtle()
 
# choose colors
colors = ["red","green","blue","yellow","purple"]
 
# decide pen size
t.pensize(3)

# choose pen color
t.pencolor("black")
 
# draw the star
t.penup()
t.setpos(-90,30)
t.pendown()

for i in range(5):
    t.pencolor(colors[i])
    t.forward(200)
    t.right(144)
 
t.penup()
t.setpos(80,-140)
t.pendown()

#