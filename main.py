import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard, border,roads,lines
from car_manager import collection
game_is_on = True


screen = Screen()
bor=border()
road=roads()
line=lines()
screen.setup(width=600, height=600)
screen.tracer(0)
player=Player()
player.move()
car = CarManager()
score=Scoreboard()
s=10
t=0.1



while game_is_on:
    time.sleep(t)
    screen.update()
    car.create_car()
    #movement of cars
    # detect collision with the cars
    if player.ycor()>300:
        screen.tracer(0)
        s=s+10
        t=t/2
        collection.clear()
        screen.clear()
        player = Player()
        player.move()
        screen.tracer(1)
        score.increaselevel()
    else:
        for carr in collection:
            if carr.xcor() > -350:
                if carr.distance(player)<20:
                    game_is_on=False
                else:
                    carr.backward(s)
            else:
                carr.hideturtle()




screen.exitonclick()