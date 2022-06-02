from turtle import Turtle, Screen 
import random

# create the screen background
screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snaky Eats its Tail")

# create snake body
seg1 = Turtle("square")
seg1.color("white")
seg1.home()

seg2 = Turtle("square")
seg2.color("white")
seg2.goto(-20, 0)

seg3 = Turtle("square")
seg3.color("white")
seg3.goto(-40, 0)
screen.exitonclick()