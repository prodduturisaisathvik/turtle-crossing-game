from turtle import Turtle

from turtle import Screen
screen=Screen()

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        screen.tracer(0)
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(0,-280)
        self.left(90)
        screen.tracer(1)


    def move(self):
        def up():
            self.forward(1)
        def down():
            self.backward(1)


        self.screen.listen()
        self.screen.onkeypress(up, "w")
        self.screen.onkeypress(down, "s")





