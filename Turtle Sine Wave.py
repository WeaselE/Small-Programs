from math import sin, radians
from turtle import Turtle,Pen,Screen

length = 1
height = 1

demo = input("Would you like to see the demo (Y/N): ")
demo = demo.upper()

# Modifiers for the sine wave
if demo != "Y":
    lengthmod = float(input("insert Length Modifier (default is 0): "))
    if lengthmod < 0:
        lengthmod = 0
    heightmod = float(input("insert Height Modifier (default is .5): "))
    if heightmod < 0:
        heightmod = 0
    wavemod = int(input("insert amount of Sine Waves (default is 1): "))
    if wavemod < 1:
        wavemod = 1
    waveamount = int(input("insert amount of Sine Wave Iterations (default is 5): "))
    if waveamount < 1:
        waveamount = 1
else:
    lengthmod = 0
    heightmod = .5
    wavemod = 1
    waveamount = 5
print("\nOn completion of your Sine Wave Drawing, click the screen to exit")

fred = Turtle()
pen = Pen()
sc = Screen()

pen.pensize(0)
pen.pencolor('white')
sc.bgcolor('gray')
pen.speed(0)
sc.reset()
count = 0

sc.setworldcoordinates(0,-3,360*wavemod,3)

while True:
    for angle in range(360 * wavemod):
        y = sin(radians(angle))
        fred.goto(angle * length,y * height)
    height = height + heightmod
    length = length + lengthmod
    fred.penup()
    fred.goto(0, 0)
    fred.pendown()
    count += 1
    if count == waveamount:
        break
sc.exitonclick()