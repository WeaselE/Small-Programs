import turtle
import random
colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
t = turtle.Pen()
t.hideturtle()
t.speed(0)
t.pensize(0)
turtle.bgcolor('black')
while True:
    for x in range(9999999):
        t.pendown()
        t.pencolor(colors[x%6])
        t.width(x/100+1)
        t.forward(x)
        t.left(59)
    # t.penup()
    # t.setpos(random.randrange(-500, 500, 10), random.randrange(-500, 500, 10))