from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.screen.tracer(0)
        self.hideturtle()
        self.level = 1
        self.penup()
        self.color("black")
        self.goto(-230,260, )
        self.write(f"LEVEL:{self.level}", align="center", font=("arial", 24, "normal"))
        self.screen.tracer(1)


    def increaselevel(self):
        self.clear()
        self.level=self.level+1
        self.write(f"LEVEL:{self.level}", align="center", font=("arial", 24, "normal"))


