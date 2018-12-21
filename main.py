import turtle

game = turtle.Screen()

game.title("Pong")
game.bgcolor("black")
game.setup(width=800, height=600)
game.tracer(0)

score_a = 0
score_b = 0
score = "Player A: " + str(score_a) + " Player B: " + str(score_b)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = -0.2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("White")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(score, align="center", font=("Arial", 8, "normal"))


# Functions

def paddle_a_up():
    if paddle_a.ycor() <= 250:
        paddle_a.sety(paddle_a.ycor() + 20)


def paddle_a_down():
    if paddle_a.ycor() >= -250:
        paddle_a.sety(paddle_a.ycor() - 20)


def paddle_b_up():
    if paddle_b.ycor() <= 250:
        paddle_b.sety(paddle_b.ycor() + 20)


def paddle_b_down():
    if paddle_b.ycor() >= -250:
        paddle_b.sety(paddle_b.ycor() - 20)


# Keyboard Binding


game.onkeypress(paddle_a_up, "w")
game.onkeypress(paddle_a_down, "s")
game.onkeypress(paddle_b_up, "Up")
game.onkeypress(paddle_b_down, "Down")
game.listen()

# MAIN Game Loop
while True:
    game.update()

    # Ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Top
    if ball.ycor() > 290:
        ball.dy *= -1

    # Border Bottom
    if ball.ycor() < -280:
        ball.dy *= -1

    # Ball Reset
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: " + str(score_a) + " Player B: " + str(score_b), align="center", font=("Arial", 8, "normal"))

    if ball.xcor() < -400:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: " + str(score_a) + " Player B: " + str(score_b), align="center", font=("Arial", 8, "normal"))

    if 340 < ball.xcor() < 350 and abs(ball.ycor() - paddle_b.ycor()) < 50:
        ball.setx(340)
        ball.dx *= -1

    if -350 < ball.xcor() < -340 and abs(ball.ycor() - paddle_a.ycor()) < 50:
        ball.setx(-340)
        ball.dx *= -1
