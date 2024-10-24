import time
from turtle import Screen
from car import Car
from CarManager import CarManager
from player import Player
from scoreboard import Scoreboard

speed = 0.1
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
timmy = Player()
#scoreboard = Scoreboard()
cars = []
screen.listen()
screen.onkeypress(timmy.move, "w")
game_is_on = True
cman = CarManager(20)
while game_is_on:
    screen.update()
    cman.move_cars(15)
    #time.sleep(speed)