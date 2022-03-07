from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

import time

# screen setting:
screen = Screen()
screen.title("Snake Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_over = False

while not game_over:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food:
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.update()
        snake.grown_up()

    # detect collision with wall:
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        scoreboard.reset()
        snake.reset()
        # scoreboard.game_over()
        # game_over = True

    # detect collision with tail:
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
            # scoreboard.game_over()
            # game_over = True


screen.exitonclick()

