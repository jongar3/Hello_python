import turtle
from turtle import Screen, mainloop
from classes import Snake, Food, do_the_thing, ScoreBoard
screen = Screen()
screen.setup(width=640, height=640)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

scoreboard = ScoreBoard()
snake= Snake()
food= Food(snake, "red")
bad_apple= Food(snake, "purple")
screen.update()
def game_loop():
    global bad_apple
    snake.forward(screen)
    game_on = not snake.kys()
    if snake.part[0].distance(food) < 15:
        food.eated()
        scoreboard.increase_score()
        snake.grow()
    elif snake.part[0].distance(bad_apple) < 15:
        bad_apple.eated()
        do_the_thing(scoreboard)
        print("You ate the bad apple")
        game_on = False
        return

    while food.position == bad_apple.position:
        bad_apple.hideturtle()
        del bad_apple
        bad_apple = Food(snake, "purple")
    if not game_on:
        scoreboard.game_over()
        print("You LOOSE")
        return

    screen.ontimer(game_loop,150)

screen.listen()
screen.onkey(key="Up",fun= snake.go_up)
screen.onkey(key="Down",fun= snake.go_down)
screen.onkey(key="Right",fun= snake.go_right)
screen.onkey(key="Left",fun= snake.go_left)


game_loop()
screen.exitonclick()
