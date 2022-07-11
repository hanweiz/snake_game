import random
from turtle import Turtle

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
        rnd_x = random.randint(-370, 370)
        rnd_y = random.randint(-370, 370)
        self.goto(rnd_x, rnd_y)
        self.count += 1