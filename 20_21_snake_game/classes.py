from turtle import Turtle
import random
import os
import subprocess
import pathlib
PATH= pathlib.Path.cwd() / "highscore.txt"
PATH_VIDEO= pathlib.Path(__file__).resolve().parent.parent / "venv" / "bin" / "bad-apple-turtle"
class Snake:
    def __init__(self):
        self.parts= 3
        self.direction_angle= 0
        self.next_direction_angle=0
        self.part=[]
        for pos in range(0,self.parts):
            self.part.append(Turtle())
            self.part[pos].color("green")
            self.part[pos].shape("square")
            self.part[pos].up()
            self.part[pos].goto(-(pos*20),0)
        self.part[0].color("lime")
        self.last_position= self.part[self.parts-1].position()
    def __upload_body(self):
        """(...) The second part of the body firsts one position. The first piece of the body will take the heads position. """
        self.last_position = self.part[self.parts - 1].position()
        for pos in range(self.parts -1, 0, -1):
            self.part[pos].goto(self.part[pos-1].position()) #(...) The second part of the body firsts one position. The first piece of the body will take the heads position.

    def forward(self,screen):
        self.__upload_body() #First we move the body
        self.part[0].setheading(self.next_direction_angle)
        self.direction_angle = self.next_direction_angle
        self.part[0].forward(20)  # Then we move the head
        screen.update()

    def go_up(self):
        if self.direction_angle !=270:
            self.next_direction_angle= 90
    def go_down(self):
        if self.direction_angle !=90:
            self.next_direction_angle= 270
    def go_left(self):
        if self.direction_angle !=0:
            self.next_direction_angle= 180
    def go_right(self):
        if self.direction_angle !=180:
            self.next_direction_angle= 0
    def grow(self):
        self.part.append(Turtle())
        self.parts+=1
        self.part[self.parts-1].color("green")
        self.part[self.parts-1].shape("square")
        self.part[self.parts-1].up()
        self.part[self.parts-1].goto(self.last_position)

    def kys(self):
        head_pos= self.part[0].position()
        for pos in range(2,self.parts):
            if self.part[0].distance(self.part[pos]) < 15:
                return True

        for axis in head_pos:
            if axis<-310 or axis>310:
                return True
        return False



class Food(Turtle):
    def __init__(self, snake, color):
        super().__init__()
        self.snake=snake #SAME OBJECT self.snake is snake = True
        self.shape("square")
        self.color(str(color))
        self.penup()
        self.__move_position()

    def __move_position(self):
        """move to a position in which the head of the snake could cross"""
        pos = (random.randint((-320 // 20) + 1, (320 // 20) - 1) * 20, random.randint((-320 // 20) + 1, (320 // 20 )- 1) * 20)
        while self.__position_on_snake(pos):
            pos = (random.randint((-320 // 20) + 1, (320 // 20) - 1) * 20, random.randint(-320 // 20 + 1, (320 // 20) - 1) * 20)
            print("a")
        print(pos)
        self.goto(pos)
    def eated(self):
        self.__move_position()
    def __position_on_snake(self, pos):
        print(self.snake.parts)
        for p in self.snake.part:
            if pos==p.position():
                return True
        return False

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0,270)
        self.hideturtle()
        self.color("White")
        if PATH.exists():
            with open(PATH, "r") as file:
                self.highscore= int(file.read())
            self.write(f"Score: {self.score}, Highscore: {self.highscore}", align="center",font=("Arial", 30, "normal"))
        else:
            self.write(f"Score: {self.score}", align="center", font=("Arial", 30, "normal"))
            self.highscore=0

    def upload_score(self):
        self.write(f"Score: {self.score}, Highscore: {self.highscore}", align="center", font=("Arial", 30, "normal"))
    def increase_score(self):
        self.score += 1
        self.clear()
        self.upload_score()
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=("Arial", 30, "normal"))
        if self.highscore<self.score:
            with open(PATH, "w") as file:
                file.write(str(self.score))

    def game_over2(self):
        self.goto(0,0)
        self.clear()
        self.write("You eat the bad apple!", align="center", font=("Arial", 30, "normal"))


def do_the_thing(board):

    #subprocess.Popen([RUTA, "--demo", "--no-vlc"])
    #subprocess.Popen([ "/home/jongar/Hello_python/venv/bin/bad-apple-turtle", "--download", "https://www.youtube.com/watch?v=c56TpxfO9q0","--no-vlc" ])
    #subprocess.Popen([
    #  "/home/jongar/Hello_python/venv/bin/bad-apple-turtle",
    # "--video", "video.mp4",
    #    "--no-vlc"
    #])
    #subprocess.Popen(["../venv/bin/bad-apple-turtle", "--demo", "--no-vlc"])
    subprocess.Popen([PATH_VIDEO, "--demo", "--no-vlc"])

    board.game_over2()