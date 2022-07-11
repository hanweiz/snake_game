import turtle
from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
STEP_DISTANCE = 20

class Snake:

    def __init__(self, shape="square", color="white"):
        self.segments = []
        self.shape = shape
        self.color = color
        self.create_snake()
        self.head = self.segments[0] 

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
    
    def add_segment(self, position):
        # increase number of segments by 1 
        segment = Turtle(self.shape)
        segment.color(self.color)
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)
    
    def extend(self):
        # create a new segment at the end of the snake
        self.add_segment(self.segments[-1].position())
     
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