import turtle
from turtle import Turtle

turtle.register_shape("rectangle", ((-25, -5), (-25, 5), (25, 5), (25, -5)))

class Pong:
    def __init__(self, color, shape, x, y):
        self.color = color
        self.shape = shape
        self.start_width = int(x)
        self.start_height = int(y)
        self.pong_turtle = None

    def setup_pong(self):
        self.pong_turtle = Turtle()
        self.pong_turtle.shape(self.shape)
        self.pong_turtle.color(self.color)
        self.pong_turtle.penup()
        self.pong_turtle.goto(self.start_width, self.start_height)

    def is_collision(self, other_turtle):
        # Check if this Pong object collides with another turtle
        return self.pong_turtle.distance(other_turtle.ball_turtle) < 20

    def easy_move_ai(self,ball_y):
        # Move the AI paddle towards the y-coordinate of the ball
        if self.pong_turtle.ycor() < ball_y:
            self.pong_turtle.sety(self.pong_turtle.ycor() + 5)
        elif self.pong_turtle.ycor() > ball_y:
            self.pong_turtle.sety(self.pong_turtle.ycor() - 5)

    def normal_move_ai(self, ball_y):
        # Move the AI paddle towards the y-coordinate of the ball
        if self.pong_turtle.ycor() < ball_y:
            self.pong_turtle.sety(self.pong_turtle.ycor() + 8)
        elif self.pong_turtle.ycor() > ball_y:
            self.pong_turtle.sety(self.pong_turtle.ycor() - 8)

    def hard_move_ai(self, ball_y):
        # Move the AI paddle towards the y-coordinate of the ball
        if self.pong_turtle.ycor() < ball_y:
            self.pong_turtle.sety(self.pong_turtle.ycor() + 10)
        elif self.pong_turtle.ycor() > ball_y:
            self.pong_turtle.sety(self.pong_turtle.ycor() - 10)