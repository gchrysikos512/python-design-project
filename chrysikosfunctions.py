import turtle
bob = turtle.Turtle()
bob.speed(0)

def polygon(distance,sides,c):
    angle = 360/sides
    c = color(color)
    bob.color(color)
    bob.begin_fill()
    for times in range(sides):
        bob.forward(distance)
        bob.right(angle)
        bob.end_fill

def jump(x,y):
    bob.penup()
    bob.goto(x,y)
    bob.pendown()

def star(d,c):
    bob.color(c)
    for times in range(5):
        bob.forward(d)
        bob.right(144)

def explosion(distance,color):
    bob.color(color)
    for times in range(8):
        bob.forward(distance)
        bob.right(135)
explosion(150,"orange")

turtle.colormode(255)
turtle.bgcolor(0,0,0)
c = (255,255,0)
