import turtle
nosides = 8
outlenght = 30
inlenght = 10
color1 = "green"
for step in range(nosides):
    turtle.colormode(color1)
    turtle.forward(outlenght)
    turtle.right(360/nosides)
    for moresteps in range(nosides):
        turtle.forward(inlenght)
        turtle.right(360/nosides)
