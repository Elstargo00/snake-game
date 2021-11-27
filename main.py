from turtle import Screen
from snake import Snake
import time

# screen setting:
screen = Screen()
screen.title("Snake Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

a_snake = Snake()

screen.listen()
screen.onkey(key="Up", fun=a_snake.up)
screen.onkey(key="Down", fun=a_snake.down)
screen.onkey(key="Left", fun=a_snake.left)
screen.onkey(key="Right", fun=a_snake.right)

game_over = False

while not game_over:
    screen.update()
    time.sleep(0.1)
    a_snake.move()


screen.exitonclick()

