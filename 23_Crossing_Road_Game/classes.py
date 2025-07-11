from turtle import Turtle
import random

SCORE_POSITION= (-300, 225)
CAR_STARTING_MOVEMENT=10
INCREMENT=5
PLAYER_STARTING_POSITION = (0, -280)
PLAYER_MOVE_DISTANCE= 10
FINISH_LINE_Y= 280
COLORS = ["red", "orange", "yellow", "green", "blue", "violet", "purple", "pink","yellow","cyan", ]
FONT= ("Courier", 24,"normal")

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.goto(PLAYER_STARTING_POSITION)

    def move(self):
        self.forward(PLAYER_MOVE_DISTANCE)

    def reset_position(self):
        self.goto(PLAYER_STARTING_POSITION)
    def player_wins(self):
        return self.ycor() >= FINISH_LINE_Y
class CarManager:
    def __init__(self):
        self.cars= []
        self.add_car()
        self.add_car()
    def add_car(self):
        car= Turtle()
        car.shape("square")
        car.color(random.choice(COLORS))
        car.penup()
        car.goto(420, random.randint(PLAYER_STARTING_POSITION[1]+ 30, FINISH_LINE_Y-20))
        car.shapesize(stretch_wid=2, stretch_len=5)
        self.cars.append(car)
    def move_cars(self, level):
        for car in self.cars.copy(): #IMPORTANT to use .copy() we are modifying the list inside the loop
            car.goto(car.xcor() - CAR_STARTING_MOVEMENT - level* INCREMENT, car.ycor())
            if car.xcor() < -460:
                self.cars.remove(car)

    def hits_player(self, player):
        for car in self.cars:
            if (abs(car.ycor()- player.ycor()) < 30) and (abs(car.xcor() - player.xcor()) < 60):
                return True

        return False



class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        self.hideturtle()
        self.goto(SCORE_POSITION)
        self.print_level(0)
    def print_level(self, level):
        self.clear()
        self.write(f"Level: {level}", align="center", font=FONT)
    def game_over(self):
        self.goto(0,0)
        self.clear()
        self.write("GAME OVER", align="center", font=FONT)