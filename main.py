from turtle import Screen 
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
HEIGHT = 800
WIDTH = 800
SLEEP = 0.1

# create the screen background
screen = Screen()
screen.setup(height=HEIGHT, width=WIDTH)
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
    time.sleep(SLEEP)        
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()
    
    # detect collision with wall
    # assumes a playing area of +-280 in both x and y axis
    if snake.head.xcor() > (WIDTH//2 - 20) or snake.head.xcor() < -(WIDTH//2 - 20) or snake.head.ycor() > (HEIGHT//2 - 20) or snake.head.ycor() < -(HEIGHT//2 - 20):
        scoreboard.game_over()
        is_game_on = False
    
    # detect collision with tail
    # idea is to check if head collides with any of the body segments
    for segment in snake.segments:
        if segment == snake.head:
            continue
        elif segment.distance(snake.head) < 10:
            scoreboard.game_over()
            is_game_on = False

screen.exitonclick()