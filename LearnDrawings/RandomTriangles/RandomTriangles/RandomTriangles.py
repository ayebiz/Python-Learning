#Idea from draw a start from StackOverFlow
#http://stackoverflow.com/questions/15748100/drawing-stars-with-turtle-in-python?rq=1
#Modify 1: try to make different types of triangles
#Modify 2: try not to overlap

import turtle
import random
#Get definations from random input
#Draw triangle using 360-240 to form a 60 degree triangle
def triangles(color, side_length, x, y):
    print(color, side_length, x, y)
    turtle.color(color)
    turtle.begin_fill()
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    for i in range(3):
        turtle.forward(side_length)
        turtle.right(240)
        turtle.forward(side_length)
    turtle.end_fill()
    #to avoid the cursor left at the drawing
    turtle.penup()
    turtle.home()

#Define the color using random color
def random_color():
    randvar = random.randrange(0, 7)
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
    elif randvar == 5:
        return ('navy')
    else:
        return ('black')

#define the triangle lenght in random
def length():
    return random.randrange(5, 71)

#define the triangle x and y co-ordinate in random
def xcoord():
    return random.randrange(-280, 281)

def ycoord():
    return random.randrange(-200, 201)

#Get input from user to get how many triangles they want
def random_triangles():
    z = int(input('How many triangles do you want?'))
    for i in range(z):
        color = random_color()
        side_length = length()
        x = xcoord()
        y = ycoord()
        triangles(color, side_length, x, y)

#Define the random triangles
random_triangles()