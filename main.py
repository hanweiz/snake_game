from turtle import Screen 
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# create the screen background
screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snaky Eats its Tail")
screen.tracer(0)

is_game_on = True
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
screen.exitonclick()

