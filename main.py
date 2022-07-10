from turtle import Turtle, Screen 
import random
import time
from snake import Snake

# create the screen background
screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snaky Eats its Tail")
screen.tracer(0)

is_game_on = True
snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
screen.exitonclick()

