import time
from turtle import Screen
from player import Player
from car_manager import CarManager, STARTING_MOVE_DISTANCE
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
sleep_time = 0.1  # Controls car speed


screen.listen()
screen.onkeypress(fun=player.move, key="w")

game_is_on = True
while game_is_on:
    time.sleep(sleep_time)
    screen.update()
    if player.ycor() >= 300:  # If player beats level
        scoreboard.next_level()
        player.goto(0, -280)
        sleep_time *= 0.9

    car_index = 0
    if not car_manager.collision(player):
        car_manager.spawn_car()
        for car in car_manager.car_list:
            car_manager.move_car(car, STARTING_MOVE_DISTANCE)
            if car.xcor() < -320:
                car_manager.car_list.remove(car_manager.car_list[car_index])
            car_index += 1
    else:
        scoreboard.game_over()
        game_is_on = False


screen.exitonclick()
