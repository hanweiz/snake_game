from turtle import Turtle, Screen 
import random
import time
import turtle

# define constants
START_SEGMENTS = 3
turtle.speed("fast")

# create the screen background
screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snaky Eats its Tail")
screen.tracer(0)

# create snake body
segments = []
for index in range(START_SEGMENTS):
    seg = Turtle("square")
    seg.color("white")
    seg.penup()
    seg.goto((index * -20), 0)
    segments.append(seg)

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)

    for seg_idx in range(len(segments) - 1, 0, -1):
        # get all segments to follow the head
        x_new = segments[seg_idx - 1].xcor()
        y_new = segments[seg_idx - 1].ycor()
        segments[seg_idx].goto(x_new, y_new)
    # then move the head
    segments[0].forward(20)
    segments[0].left(90)
screen.exitonclick()

