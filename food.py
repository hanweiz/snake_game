import random
from turtle import Turtle
import config

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("blue")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.count = 0
        self.refresh()
    
    def refresh(self):
        rnd_x = random.randint(-(config.WIDTH - 30), config.WIDTH - 30)
        rnd_y = random.randint(-(config.WIDTH - 30), config.WIDTH - 30)
        self.goto(rnd_x, rnd_y)
        self.count += 1