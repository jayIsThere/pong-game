from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=780, height=700, startx=-100, starty=-100)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")


is_go_on = True

while is_go_on:
    time.sleep(ball.speed)
    screen.update()
    ball.move()
    scoreboard.update_scoreboard()

    #collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #collision with paddles
    if ball.distance(r_paddle) < 65 or ball.distance(l_paddle) < 65:
        if ball.xcor() > 330 or ball.xcor() > -330:
            ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

    if scoreboard.l_score == 5 or scoreboard.r_score == 5:
        is_go_on = False


screen.exitonclick()