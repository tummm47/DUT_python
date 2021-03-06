from turtle import Turtle, Screen
import time

from snake import Snake
from food import Food
from scoreboard import Scoreboard
""""Set up screen"""
screen = Screen()
screen.setup(width= 600, height= 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

"""Snake Body"""
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_win = True
while is_win:
    screen.update()
    time.sleep(0.1)

    snake.move()

    #Food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_tail()
        scoreboard.plus_score()

    #Wall
    elif snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        is_win = False
        scoreboard.game_over()
    #Tail
    for part in snake.body[1:]:
        if snake.head.distance(part) < 10:
            is_win = False
            scoreboard.game_over()






screen.exitonclick()