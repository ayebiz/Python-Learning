#Learn how to use Turtle
#Try to deploy as much Turtle function as possible
import turtle
nosides = 15
outlenght = 60
inlenght = 20
#Set variables to zero
nosides = 0
outlength = 0
inlength = 0
#Define number of sides
nosides = 24
#Define the outer length of the object
outlenght = 15
#Define the inner length of the object
inlenght = 8
#Define the color of the pen for outer and inner object
color1 = "blue"
color2 = "red"
#Move pen to a new position without drawing and report pen position
turtle.penup()
print(turtle.position())
turtle.forward(-275)
#Define how the pen move and report pen position
turtle.forward(-205)
print(turtle.position())
turtle.left(45)
print(turtle.position())
turtle.left(120)
print(turtle.position())
turtle.pendown()
#Draw the pattern
for step in range(nosides):
    turtle.color(color1)
    turtle.pensize(3)
    turtle.forward(outlenght)
    turtle.right(360/nosides)
    print(turtle.position())
    for moresteps in range(nosides):
        turtle.pensize(1)
        turtle.color(color2)
        turtle.forward(inlenght)
        turtle.right(360/nosides)
turtle.penup()
turtle.home()  
#Draw 2nd pattern
#Draw the pattern
turtle.pendown()
for step in range(nosides):
    turtle.color(color1)
    turtle.pensize(3)
    turtle.forward(outlenght)
    turtle.right(360/nosides)
    print(turtle.position())
    for moresteps in range(nosides):
        turtle.pensize(1)
        turtle.color(color2)
        turtle.forward(inlenght)
        turtle.right(360/nosides)  
