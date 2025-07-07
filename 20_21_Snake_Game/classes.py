from turtle import Turtle
import random

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
        print(self.last_position)
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



class Food:
    def __init__(self, snake):
        self.snake=snake #SAME OBJECT self.snake is snake = True
        self.apple= Turtle()
        self.apple.shape("square")
        self.apple.color("red")
        self.apple.penup()
        self.__move_position()

    def __move_position(self):
        """move to a position in which the head of the snake could cross"""
        pos = (random.randint(-320 // 20 - 1, 320 // 20 - 1) * 20, random.randint(-320 // 20 - 1, 320 // 20 - 1) * 20)
        while self.__position_on_snake(pos):
            pos = (random.randint(-320 // 20 - 1, 320 // 20 - 1) * 20, random.randint(-320 // 20 - 1, 320 // 20 - 1) * 20)
        self.apple.goto(pos)
    def eated(self):
        self.__move_position()
    def __position_on_snake(self, pos):
        for p in self.snake.part:
            if pos==p.position():
                return True
        return False

