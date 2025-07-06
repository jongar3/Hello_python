import turtle as t
counter=0

cursor= t.Turtle()
screen = t.Screen()
def turn_left():
    cursor.setheading(cursor.heading()+10)
def switch_drawing():
    global counter
    if counter % 2 == 0:
        cursor.up()
    else:
        cursor.down()
    counter += 1


screen.listen()
screen.onkey(key="w", fun= lambda : cursor.forward(10))
screen.onkey(key="s", fun= lambda : cursor.backward(10))
screen.onkey(key="a", fun= turn_left)
screen.onkey(key="d", fun= lambda : cursor.right(10))
screen.onkey(key="space", fun= switch_drawing)
screen.onkey(key="c", fun= lambda : cursor.clear())


screen.exitonclick()