import turtle as t
from classes import Pong, Ball, ScoreBoard

def define_screen():
    screen = t.Screen()
    screen.bgcolor("black")
    screen.setup(width=800, height=600)
    screen.title("Pong")
    screen.tracer(0)
    pencil= t.Turtle()
    pencil.pencolor("white")
    pencil.penup()
    pencil.goto(0,-300)
    pencil.pensize(4)
    pencil.left(90)
    for j in range(15):
        pencil.pendown()
        pencil.forward(30)
        pencil.up()
        pencil.forward(40)
    return screen




INITIAL_POS_X=350
player1= Pong(INITIAL_POS_X)
player2 = Pong(-INITIAL_POS_X)
player1_score= ScoreBoard(150)
player2_score= ScoreBoard(-150)
screen = define_screen()
ball=Ball()

#Take the state of the keys.
keys_pressed = {
    "Up": False,
    "Down": False,
    "w": False,
    "s": False
}

#We use a function that returns another function (With no arguments) to use it on keypress.
def key_down(key):
    def inner():
        keys_pressed[key] = True
    return inner

def key_up(key):
    def inner():
        keys_pressed[key] = False
    return inner

#Define the game loop.
def game_loop():
    global ball
    if keys_pressed["Up"]:
        player1.go_up()
    if keys_pressed["Down"]:
        player1.go_down()
    if keys_pressed["w"]:
        player2.go_up()
    if keys_pressed["s"]:
        player2.go_down()
    ball.move()
    ball.paddle_collision(player1)
    ball.paddle_collision(player2)
    if ball.xcor() < -380:
        ball.hideturtle()
        del ball
        ball=Ball()
        player1_score.add_score()
    elif ball.xcor() > 380:
        ball.hideturtle()
        del ball
        ball = Ball()
        player2_score.add_score()
    screen.update()
    screen.ontimer(game_loop, 18)

#Take the states of the keyboard keys.
screen.listen()
screen.onkeypress(key_down("Down"), "Down") #The output of key_down("Down") will be inner()
screen.onkeypress(key_down("Up"), "Up")
screen.onkeypress(key_down("w"), "w")
screen.onkeypress(key_down("s"), "s")
screen.onkeyrelease(key_up("Down"), "Down")
screen.onkeyrelease(key_up("Up"), "Up")
screen.onkeyrelease(key_up("w"), "w")
screen.onkeyrelease(key_up("s"), "s")

game_loop()
screen.exitonclick()