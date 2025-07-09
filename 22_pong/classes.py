from turtle import Turtle, Screen
import random
import time

PONG_SPEED= 10
BALL_BASE_SPEED= 5
class Pong(Turtle):
    def __init__(self, x):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.penup()
        self.goto(x, 0)
    def go_up(self):
        x_pos = self.xcor()
        y_pos=self.ycor()
        if y_pos < 240:
            self.goto(x_pos, y_pos + PONG_SPEED)

    def go_down(self):
        x_pos = self.xcor()
        y_pos = self.ycor()
        if y_pos > -240:
            self.goto(x_pos, y_pos - PONG_SPEED)

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.angle= (random.randint(-65,65)+360)%360
        self.start= time.time()

        self.setheading(self.angle)
    def move(self):
        self.__wall_bounce()
        self.forward(BALL_BASE_SPEED+ (time.time() - self.start) // 5)

    def __wall_bounce(self):
        y_cor = self.ycor()
        if y_cor <= -290 or y_cor >= 290:
            self.angle = -self.heading()
            self.setheading(self.angle)

    def __going_right(self):
        if self.angle%360< 90 or self.angle%360> 270:
            return True
        else:
            return False

    def paddle_collision(self, paddle):
        if abs(self.ycor() - paddle.ycor()) < 50 and abs(self.xcor() - paddle.xcor()) < 20:
            current_heading = self.heading()
            self.angle = (180 - current_heading) % 360


            offset = self.ycor() - paddle.ycor()
            self.angle += offset * 0.25

            self.setheading(self.angle)
            self.forward((time.time() - self.start) // 5)


class ScoreBoard(Turtle):
    def __init__(self, x):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(x, 220)
        self.color("white")
        self.__write_score()

    def __write_score(self):
        self.clear()
        self.write(str(self.score), align="center", font=("Arial", 45, "bold"))
    def add_score(self):
        self.score+=1
        self.__write_score()