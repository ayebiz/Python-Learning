import turtle
nosides = 8
outlenght = 60
inlenght = 20
color1 = "blue"
color2 = "red"
turtle.penup()
print(turtle.position())
turtle.forward(-75)
print(turtle.position())
print(turtle.position())
turtle.left(90)
print(turtle.position())
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
turtle.penup()
turtle.home()    