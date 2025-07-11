import random
import time
from turtle import Screen
from classes import Player, CarManager, ScoreBoard

screen = Screen()
screen.setup(800, 600)
screen.tracer(0)

key_state= {"Space": False }
player= Player()
car_manager = CarManager()
scoreboard = ScoreBoard()
level=0

def press_key(key):
    def inner():
        key_state["Space"] = True
    return inner
def release_key(key):
    def inner():
        key_state["Space"] = False
    return inner

def game_loop():
    global level
    if key_state["Space"]:
        player.move()
    for _ in range(0, random.randint(-25 + level,3)):
        car_manager.add_car()
    car_manager.move_cars(level)
    screen.update()
    if player.player_wins():
        player.reset_position()
        level+=1
        scoreboard.print_level(level)
        time.sleep(1)
    elif car_manager.hits_player(player):
        scoreboard.game_over()
        return
    screen.ontimer(game_loop, 100)
screen.listen()

screen.onkeypress(press_key("Space"), "space")
screen.onkeyrelease(release_key("Space"), "space")
game_loop()
screen.exitonclick()