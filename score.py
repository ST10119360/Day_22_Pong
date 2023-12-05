from turtle import Turtle

class Score:
    def __init__(self):
        self.snake_score = Turtle()
        self.snake_score.color("white")
        self.snake_score.penup()
        self.snake_score.hideturtle()
        self.snake_score.goto(0, 280)
        self.player_score = 0
        self.cpu_score = 0
        self.update_score()

    def update_score(self):
        self.snake_score.clear()
        self.snake_score.write(f"Player: {self.player_score} | CPU: {self.cpu_score}", align="center", font=("Arial", 12, "normal"))

    def increase_player_score(self):
        self.player_score += 1
        self.update_score()

    def increase_cpu_score(self):
        self.cpu_score += 1
        self.update_score()
