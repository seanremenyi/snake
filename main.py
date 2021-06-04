from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Python Game")
screen.tracer(0)

snake_body = []
x_positions = [0, -20, -40]

for turtles in range(0,3):
    new_turtle = Turtle(shape="square")
    new_turtle.color("white")
    new_turtle.penup()
    new_turtle.goto(x=x_positions[turtles], y=0)
    snake_body.append(new_turtle)


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for segment in snake_body:
        segment.forward(20)


screen.exitonclick()