from turtle import Screen
import time
from snake import Snake, random_color
from food import Food
from scoreboard import Scoreboard
game_is_on = True
"""Manage the screen."""
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.colormode(255)

snake = Snake()
foodP = Food(True)
foodNP = Food(False)
score_board = Scoreboard()

screen.listen()
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")
while game_is_on:
    screen.bgcolor(random_color())
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with food
    if snake.segments[0].distance(foodP) < 15:
        foodP.remove_text()
        foodNP.remove_text()
        foodP.refresh()
        foodNP.refresh()
        snake.create_segment(snake.segments[-1].position())
        score_board.increase_score()

    elif snake.segments[0].distance(foodNP) < 15:
        #screen.mainloop()
        game_is_on = False
        score_board.game_over()
    elif snake.segments[0].xcor() > 290 or snake.segments[0].xcor() < -290 or snake.segments[0].ycor() > 290 or snake.segments[0].ycor() < -290:
        game_is_on = False
        score_board.game_over()
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            game_is_on = False
            score_board.game_over()
screen.exitonclick()