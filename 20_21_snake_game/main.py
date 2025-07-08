import time
from turtle import Screen, mainloop
from classes import Snake, Food, do_the_thing, ScoreBoard
screen = Screen()
screen.setup(width=640, height=640)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

scoreboard = ScoreBoard()
game_on=True
snake= Snake()
food= Food(snake)
screen.update()
def game_loop():
    snake.forward(screen)
    if snake.part[0].distance(food) < 15:
        food.eated()
        scoreboard.increase_score()
        snake.grow()
    game_on = not snake.kys()
    if not game_on:
        do_the_thing()
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
