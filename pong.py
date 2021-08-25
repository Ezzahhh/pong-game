from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x: int, y: int) -> None:
        super().__init__()
        self.create_paddle(x, y)

    def create_paddle(self, x: int, y: int) -> None:
        self.penup()
        self.shape("square")
        self.speed(0)
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1, outline=None)
        self.setpos(x, y)

    def up(self) -> None:
        x, y = self.pos()
        self.goto(x, y + 20)

    def down(self) -> None:
        x, y = self.pos()
        self.goto(x, y - 20)


class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1, outline=None)
        self.setpos(0, 0)
        self.x_move = 10
        self.y_move = 10
        self.bounce_count = 0
        self.move_speed = 0.05

    def move(self) -> None:
        x, y = self.xcor(), self.ycor()
        self.goto(x + self.x_move, y + self.y_move)

    def bounce(self) -> None:
        self.y_move *= -1

    def bounce_paddle(self) -> None:
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset(self) -> None:
        self.home()
        self.bounce()
        self.bounce_paddle()
        self.move_speed = 0.05
