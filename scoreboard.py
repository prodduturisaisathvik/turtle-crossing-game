from turtle import Turtle
cor=[0,40,-40,80,-80,120,-120,160,-160,200,-200,240,-240,-280]

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


class border(Turtle):
    def __init__(self):
        super().__init__()
        self.screen.tracer(0)
        self.hideturtle()
        self.level = 1
        self.penup()
        self.color("black")
        self.goto(-300, 300)
        self.pendown()
        self.goto(-300, -300)
        self.goto(300, -300)
        self.goto(300, 300)
        self.goto(-300, 300)



class roads(Turtle):
    def __init__(self):
        super().__init__()
        self.screen.tracer(0)
        self.hideturtle()
        self.penup()
        self.color("black")

        # Top side of road
        # Upper road
        # Top side of road

        self.goto(300, 260)
        self.pendown()
        self.goto(-300, 260)
        self.penup()

        self.goto(300, 220)
        self.pendown()
        self.goto(-300, 220)
        self.penup()

        self.goto(300, 180)
        self.pendown()
        self.goto(-300, 180)
        self.penup()

        self.goto(300, 140)
        self.pendown()
        self.goto(-300, 140)
        self.penup()

        self.goto(300, 100)
        self.pendown()
        self.goto(-300, 100)
        self.penup()

        self.goto(300, 60)
        self.pendown()
        self.goto(-300, 60)
        self.penup()

        # Middle divider
        self.goto(300, 20)
        self.pendown()
        self.goto(-300, 20)
        self.penup()

        # Bottom side of road
        self.goto(300, -20)
        self.pendown()
        self.goto(-300, -20)
        self.penup()

        self.goto(300, -60)
        self.pendown()
        self.goto(-300, -60)
        self.penup()

        self.goto(300, -100)
        self.pendown()
        self.goto(-300, -100)
        self.penup()

        self.goto(300, -140)
        self.pendown()
        self.goto(-300, -140)
        self.penup()

        self.goto(300, -180)
        self.pendown()
        self.goto(-300, -180)
        self.penup()

        self.goto(300, -220)
        self.pendown()
        self.goto(-300, -220)
        self.penup()

        self.goto(300, -260)
        self.pendown()
        self.goto(-300, -260)
        self.penup()

class lines(Turtle):
    def __init__(self):
        super().__init__()
        self.screen.tracer(0)
        self.hideturtle()
        self.setheading(180)
        for c in cor:
            self.penup()
            self.goto(300,c)
            while self.xcor()>-300:
                self.color("black")
                self.pendown()
                self.forward(10)
                self.penup()
                self.forward(10)



