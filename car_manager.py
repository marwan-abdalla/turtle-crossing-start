import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.random = random.randint(-280, 250)
        self.move_increment = MOVE_INCREMENT
        self.color(random.choice(COLORS))
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=2)
        self.goto(280, self.random)

    def moving_left(self):
        new_x = self.xcor() - self.move_increment
        self.goto(new_x, self.random)

    def increasing_speed(self):
        self.move_increment += 5
        self.moving_left()








