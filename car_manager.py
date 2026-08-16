from turtle import Turtle
import random

from turtle import Screen
flow=True


screen=Screen()

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
cor=[0,40,-40,80,-80,120,-120,160,-160,200,-200,240,-240,-280]
collection=[]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
x=280



class CarManager:
    def __init__(self):
        pass


    def create_car(self):
        screen.tracer(0)
        car=Turtle()
        car.penup()
        car.shape("square")
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.color(random.choice(COLORS))
        car.goto(x,y=random.choice(cor) )
        screen.tracer(1)
        collection.append(car)











