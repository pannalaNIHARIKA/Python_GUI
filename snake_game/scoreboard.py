from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as hscore:
            self.highscore = int(hscore.read())
        self.hideturtle()
        self.penup()
        self.pencolor("white")
        self.goto(0,270)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"score = {self.score} , Highscore = {self.highscore}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT,font=FONT)
    def reset(self):
        if self.score > self.highscore :
            self.highscore = self.score
            with open("data.txt",mode="w") as hscore:
                hscore.write(f"{self.highscore}")
        self.score = 0
        self.update_score()


