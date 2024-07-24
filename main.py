import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

current_score = Scoreboard()
cars = []
player = Player()

screen.onkey(player.move, "Up")

game_is_on = True
car_spawn_chance = 0.2

while game_is_on:
    time.sleep(0.1)
    screen.update()

    if random.random() < car_spawn_chance:
        car = CarManager()
        cars.append(car)

    for car in cars:
        car.moving_left()

        if player.distance(car) < 20:
            current_score.game_over()
            game_is_on = False

    if player.ycor() > 270:
        current_score.update_level()
        player.reset_position()
        car_spawn_chance += 0.1
        for car in cars:
            car.increasing_speed()




screen.exitonclick()



