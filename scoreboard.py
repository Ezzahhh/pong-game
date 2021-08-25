from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 40, "bold")


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = [0, 0]
        self.score_logic()

    def add_score_left(self) -> None:
        self.reset()
        self.score[0] += 1
        self.score_logic()

    def add_score_right(self) -> None:
        self.reset()
        self.score[1] += 1
        self.score_logic()

    def score_logic(self):
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 230)
        self.write(
            f"{self.score[0]} : {self.score[1]}",
            align=ALIGNMENT,
            font=FONT,
        )
