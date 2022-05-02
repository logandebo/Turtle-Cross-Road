from turtle import Turtle
from random import randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.setx(30)
        self.sety(280)
        self.shape("turtle")
        self.setheading(270)
        self.car_list = []

    def spawn_car(self):
        if len(self.car_list) <= 40:
            rand_num = randint(1, 5)  # Controls frequency of car spawn
            if rand_num == 1:
                new_car = Turtle()
                new_car.penup()
                new_car.color(COLORS[randint(0, 5)])
                new_car.shape("square")
                new_car.shapesize(stretch_wid=1, stretch_len=2)
                new_car.setx(310)
                new_car.sety(randint(-250, 250))
                new_car.setheading(180)
                self.car_list.append(new_car)

    def move_car(self, car, distance):
        car.forward(distance)

    def collision(self, player):
        for car in self.car_list:
            if 27 >= car.ycor() - player.ycor() >= -18 and -30 <= car.xcor() - player.xcor() <= 30:
                return True
