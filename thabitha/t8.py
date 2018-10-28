import turtle
import random

# setup the window with a background colour
wn = turtle.Screen()
wn.bgcolor("#EFECCA")
wn.setup(width=250, height=250) 

# give a random name to your turtle
turtle = turtle.Turtle()

colors = ["#7D8A2E", "#263248", "#FF8C00", "#F0C600"]

#
def snowflake(size, pensize, x, y):
    """ function that draws a snowflake """
    # turtle.pen(pensize=10)
    turtle.penup()
    turtle.goto(x, y)
    turtle.forward(10*size)
    turtle.left(45)
    turtle.pendown()
    turtle.color(random.choice(colors))

    for i in range(8):
        branch(size)
        turtle.left(45)


# for one branch of the snowflake
def branch(size):
    for i in range(3):
        for i in range(3):
            turtle.forward(10.0*size/3)
            turtle.backward(10.0*size/3)
            turtle.right(45)
        turtle.left(90)
        turtle.backward(10.0*size/3)
        turtle.left(45)
    turtle.right(90)
    turtle.forward(10.0*size)

snowflake(8, 6, 0, 0)

# leave the window open until you wanna end the program
#goodluck
wn.exitonclick()
