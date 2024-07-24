from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("Red")
        self.hideturtle()
        self.penup()
        self.goto(-230, 250)
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def update_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def game_over(self):
        self.color("Red")
        self.hideturtle()
        self.penup()
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 50, "normal"))

