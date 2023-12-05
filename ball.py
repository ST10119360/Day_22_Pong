# ball.py
import random
from turtle import Turtle

from pong import Pong

class Ball:
    def __init__(self, color, shape, x, y):
        self.color = color
        self.shape = shape
        self.xvalue = int(x)
        self.yvalue = int(y)
        self.ball_turtle = None
        self.pong_instance = Pong("white", "rectangle", 0, 0)  # Create an instance of the Pong class

    def setup_ball(self):
        self.ball_turtle = Turtle()
        self.ball_turtle.shape(self.shape)
        self.ball_turtle.color(self.color)
        self.ball_turtle.shapesize(0.5, 0.5)
        self.ball_turtle.penup()
        self.ball_turtle.goto(self.xvalue, self.yvalue)
        # You need to add a line here to set a random initial heading
        self.ball_turtle.setheading(random.randint(0, 360))

    def ball_move(self):
        self.ball_turtle.forward(15)

    def bounce(self):
        current_heading = self.ball_turtle.heading()
        # Reflect the angle upon collision
        self.ball_turtle.setheading(180 - current_heading)
        self.ball_turtle.forward(10)

    def is_out_of_bounds(self):
        return not (-300 < self.ball_turtle.xcor() < 300)  # Adjust the bounds as needed

    def refresh(self):
        self.ball_turtle.goto(0, 0)
        self.ball_turtle.setheading(random.randint(0, 360))  # Set a random initial angle
