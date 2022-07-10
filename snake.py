import turtle
from turtle import Turtle, Screen

START_SEGMENTS = 3
STEP_DISTANCE = 20
class Snake:

    def __init__(self, initial_segments = START_SEGMENTS, color = "white", shape = 'square'):
        self.segments = []
        self.color = color
        self.shape = shape
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for index in range(START_SEGMENTS):
            seg = Turtle(self.shape)
            seg.color(self.color)
            seg.penup()
            seg.goto((index * -20), 0)
            self.segments.append(seg)
    
    def move(self):
        for seg_idx in range(len(self.segments) - 1, 0, -1):
            # get all segments to follow the head
            x_new = self.segments[seg_idx - 1].xcor()
            y_new = self.segments[seg_idx - 1].ycor()
            self.segments[seg_idx].goto(x_new, y_new)
        self.head.forward(STEP_DISTANCE)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
        
    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
    
    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
    
    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)