
import turtle
bob = turtle.Turtle()
turtle.bgcolor(0,0,0)
turtle.colormode(255)
bob.speed(0)
bob.color("brown")

side=200
bob.penup()
bob.goto(-100,-100)
bob.pendown()

for times in range (100,200):
   bob.forward(side)
   bob.left(90)
   side=side-4

bob.penup()
bob.goto(200,200)
bob.pendown()
bob.color("orange")
for times in range (100,200):
   bob.forward(side)
   bob.left(90)
   side=side-1

bob.penup()
bob.goto(-150,-200)
bob.pendown()
bob.color("red")
for times in range (100,200):
   bob.forward(side)
   bob.left(90)
   side=side-2


bob.penup()
bob.goto(-150,200)
bob.pendown()

bob.color("cyan")
for times in range (100,200):
   bob.forward(side)
   bob.left(90)
   side=side-2

bob.penup()
bob.goto(150,-150)
bob.pendown()

bob.color("yellow")
for times in range (100,200):
   bob.forward(side)
   bob.left(90)
   side=side-2



   
