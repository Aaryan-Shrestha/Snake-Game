from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Algerian", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.pendown()
        self.increment_score()
        self.hideturtle()

    def increment_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)
        self.score += 1

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="Game Over!!!", move=False, align=ALIGNMENT, font=FONT)