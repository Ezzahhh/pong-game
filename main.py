from turtle import Screen
from scoreboard import Scoreboard
from pong import Paddle, Ball
import time

screen = Screen()
screen.cv._rootwindow.resizable(False, False)
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
screen.listen()

right_paddle = Paddle(350, 0)
left_paddle = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.onkeypress(key="Up", fun=right_paddle.up)
screen.onkeypress(key="Down", fun=right_paddle.down)

screen.onkeypress(key="w", fun=left_paddle.up)
screen.onkeypress(key="s", fun=left_paddle.down)

is_running = True
while is_running:
    if ball.bounce_count != 0:
        time.sleep(ball.move_speed)
    else:
        time.sleep(0.05)
    screen.update()
    ball.move()

    if abs(ball.ycor()) > 280:
        ball.bounce()

    if ball.xcor() > 380:
        # Add to score of Left and reset ball
        scoreboard.add_score_left()
        ball.reset()

    elif ball.xcor() < -380:
        # Add to score of Right and reset ball
        scoreboard.add_score_right()
        ball.reset()

    if (
        (ball.xcor() > 325)
        and (ball.distance(right_paddle) < 45)
        or (ball.xcor() < -325)
        and (ball.distance(left_paddle) < 45)
    ):
        ball.bounce_paddle()


screen.exitonclick()
