from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.speed("fastest")
        self.level = 1
        self.goto(x=-200, y=250)
        self.write(arg=f"Level: {self.level}", align="center", font=FONT)

    def next_level(self):
        self.level += 1
        self.clear()
        self.goto(x=-200, y=250)
        self.write(arg=f"Level: {self.level}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="Game Over.", align="center", font=FONT)