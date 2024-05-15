import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


scoreboard = Scoreboard()
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player = Player()
carmgr= CarManager()
screen.onkey(player.move_up,"Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    carmgr.create_car()
    carmgr.move_cars()

    for car in carmgr.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    if(player.is_at_finish_line()):
        player.go_to_start()
        carmgr.level_up()
        scoreboard.increase_level()





screen.exitonclick()
