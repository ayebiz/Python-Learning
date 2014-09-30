#Draw a star from StackOverFlow
#http://stackoverflow.com/questions/15748100/drawing-stars-with-turtle-in-python?rq=1
#Find error at random_color section and make changes by adding random to random.randrange(0,5)

import turtle
import random

def star(color, side_length, x, y):
    print(color, side_length, x, y)
    turtle.color(color)
    turtle.begin_fill()
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    for i in range(5):
        turtle.forward(side_length)
        turtle.right(144)
        turtle.forward(side_length)
    turtle.end_fill()
    turtle.penup()
    turtle.home()


def random_color():
    randvar = random.randrange(0, 5)
    if randvar == 0:
        return ('red')
    elif randvar == 1:
        return ('blue')
    elif randvar == 2:
        return ('green')
    elif randvar == 3:
        return ('yellow')
    elif randvar == 4:
        return ('purple')
    else:
        return ('black')


def length():
    return random.randrange(5, 71)


def xcoord():
    return random.randrange(-280, 281)


def ycoord():
    return random.randrange(-200, 201)


def night_sky():
    z = int(input('How many stars do you want?'))
    for i in range(z):
        color = random_color()
        side_length = length()
        x = xcoord()
        y = ycoord()
        star(color, side_length, x, y)

night_sky()