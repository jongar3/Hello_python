import turtle
from turtle import *
import heroes as h
from random import randint
print(h.gen())
timmy_the_turtle=Turtle()
def square(turtle, size):
    for i in range(0, 4):
        turtle.forward(size)
        turtle.left(90)
def dash_line(turtle =timmy_the_turtle, number=5):
    for i in range(0, number):
        turtle.forward(20)
        turtle.up()
        turtle.forward(20)
        turtle.down()
def draw_figures(turtle, size):

    for j in range(3,11):
        tracer(0)
        for i in range(0,j):
            turtle.forward(size)
            turtle.left(360/j)
        turtle.color(randint(0, 255)/255, randint(0, 255)/255, randint(0, 255)/255)
    tracer(1)

def random_walk(turtle, number):
    turtle.pensize(12)
    for i in range(0, number):
        turtle.color(randint(0, 255) / 255, randint(0, 255) / 255, randint(0, 255) / 255)
        turtle.right(90 * randint(0, 3))
        turtle.forward(20)

def spirograph(turtle, number):
    tracer(0)
    for i in range(0, number):
        turtle.color(randint(0, 255) / 255, randint(0, 255) / 255, randint(0, 255) / 255)
        turtle.circle(100)
        turtle.right(360/number)
    tracer(1)



timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("PaleVioletRed2")


#square(timmy_the_turtle, 100)
#dash_line(timmy_the_turtle, 6)
#draw_figures(timmy_the_turtle, 100)
#random_walk(timmy_the_turtle, 100)
#spirograph(timmy_the_turtle, 50)


screen = Screen()
screen.listen()
screen.onkey(key= "space", fun= dash_line)

screen.exitonclick()
