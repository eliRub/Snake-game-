import time
from turtle import Screen
from snake import Snake
from food import Food
from score_board import ScoreBoard

# file = open("data.txt")
# contents = file.read()
# file.close()
#
# with open("data.txt", mode='r') as file: # 'mode' by default = 'r'
#     contents = file.read()
#
# with open("data.txt", mode='w') as file:   w, r, a
#     contents = file.read()
screen = Screen()
screen.setup(600, 550)
screen.title("My Snake Game.")
screen.bgcolor("black")
screen.tracer(0)  # this get positive/negative numbers, and turn off the animation,
# and wait for the update() to declare on drawing. it can be used only once.

screen.listen()
snake = Snake()
food = Food()
score_board = ScoreBoard()

screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_right, "Right")
screen.onkey(snake.move_left, "Left")

is_on = True
while is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh_location()
        score_board.increase_score()
        snake.extend()

    if snake.head.xcor() >= 305 or snake.head.xcor() <= -305 or snake.head.ycor() >= 280 or snake.head.ycor() <= -280:
        score_board.reset()
        snake.reset()

    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            score_board.reset()
            snake.reset()

screen.exitonclick()
