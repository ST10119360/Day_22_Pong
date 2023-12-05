"""
Pong
The game must have an AI controlled component and a user controlled
The objects can only go up and down
Must keep score based on which side the ball goes
The ball must start from center and head a random direction from the center
when ball makes contact it must change direction, and it angles
game continues until 10

"""
import time
from turtle import Screen

import pong
import ball
import score

game_is_on = True
player_score = 0
cpu_score = 0
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)
pongs_player = pong.Pong("white", "rectangle", -275, 0)
pongs_player.setup_pong()

pongs_ai = pong.Pong("white", "rectangle", 275, 0)
pongs_ai.setup_pong()

pong_ball = ball.Ball("white", "circle", 0, 0)
pong_ball.setup_ball()

scores = score.Score()


def move_up():
    y = pongs_player.pong_turtle.ycor()
    if y < 250:  # Limit the movement to avoid going off the screen
        pongs_player.pong_turtle.sety(y + 20)


# Function to move the player's paddle down
def move_down():
    y = pongs_player.pong_turtle.ycor()
    if y > -240:  # Limit the movement to avoid going off the screen
        pongs_player.pong_turtle.sety(y - 20)


user = screen.textinput("Difficulty", "What difficulty do you want")
if user == "easy":
    pong_ai_move = pongs_ai.easy_move_ai
elif user == "normal":
    pong_ai_move = pongs_ai.normal_move_ai
else:
    pong_ai_move = pongs_ai.hard_move_ai
# Listen for keypress events
screen.listen()
screen.onkeypress(move_up, "w")
screen.onkeypress(move_down, "s")
while game_is_on:

    time.sleep(0.1)
    pong_ball.ball_move()
    pong_ai_move(pong_ball.ball_turtle.ycor())
    screen.update()
    if (
            pongs_player.is_collision(pong_ball) or
            pongs_ai.is_collision(pong_ball)
    ):
        pong_ball.bounce()

    # Check if the ball hits the top or bottom of the screen
    if (
            pong_ball.ball_turtle.ycor() > screen.window_height() / 2 - 15 or
            pong_ball.ball_turtle.ycor() < -screen.window_height() / 2 + 15
    ):
        # Reverse the y-direction to make the ball bounce off the top or bottom
        pong_ball.ball_turtle.setheading(-pong_ball.ball_turtle.heading())

    if pong_ball.is_out_of_bounds():
        if pong_ball.ball_turtle.xcor() < 0:
            scores.increase_cpu_score()
            pong_ball.refresh()
            pass
        else:
            scores.increase_player_score()
            pong_ball.refresh()
            pass

screen.exitonclick()
