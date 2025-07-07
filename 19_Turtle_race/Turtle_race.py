import turtle as t
from random import choice, randint
screen=t.Screen()
screen.setup(width=500, height=400)

leonardo=t.Turtle()
leonardo.color("blue")
leonardo.name="leonardo"

raphael=t.Turtle()
raphael.color("red")
raphael.name="raphael"

donatelo=t.Turtle()
donatelo.color("purple")
donatelo.name="donatelo"

michelangelo=t.Turtle()
michelangelo.color("orange")
michelangelo.name="michelangelo"

turtle_list=(leonardo,raphael, michelangelo, donatelo)
cont=0
colors=[]
for turtle in turtle_list:
    cont += 1
    colors.append(turtle.color()[0])
    turtle.shape("turtle")
    turtle.up()
    turtle.goto(y= 250 - cont* 100,x=-250 + 15 )
    turtle.down()

bet= screen.textinput(title="Who is going to win?", prompt="Which turtle will win? insert the color: (red/blue/purple/orange)").lower()
while bet not in colors:
    bet=screen.textinput(title="NOT VALID COLOR", prompt="Which turtle will win? insert the color: (red/blue/purple/orange)").lower()

winner=None
if bet:
    winner= "start"
while winner == "start":
    ninja_turtle=choice(turtle_list) #In this case we avoid the draw
    ninja_turtle.forward(randint(0, 4))
    if ninja_turtle.pos()[0]>230:
        winner=ninja_turtle
        print("The winner is " + winner.name)
        print("You Win!" if winner.color()[0] == bet else "You Lose!")

screen.exitonclick()