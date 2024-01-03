from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.read_file()
        self.color("pink")
        self.penup()
        self.hideturtle()
        self.goto(0, 210)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}   High Score: {self.high_score}", False, ALIGNMENT, FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_file()
        self.score = 0
        self.update_scoreboard()

    def write_file(self):
        with open("data.txt", mode='w') as file:
            file.write(str(f"{self.high_score}"))

    def read_file(self) -> int:
        with open("data.txt", mode='r') as file:
            data = int(file.read())
        return data

    # def game_over(self):
    #     self.home()
    #     self.write("Game Over.", False, ALIGNMENT, FONT)
