import  turtle
import  random
import  time
speed=0.1
wn=turtle.Screen()
wn.title("snake-Game")
wn.bgcolor("black")
wn.setup(width=1200,height=800)
wn.tracer(0)



snake=turtle.Turtle()
snake.speed(0)
snake.shape("square")
snake.shapesize(stretch_wid=1,stretch_len=1)
snake.color('white')
snake.penup()
snake.goto(-350,0)
snake.direction="stop"



point=turtle.Turtle()
point.speed(0)
point.shape('circle')
point.shapesize(stretch_wid=1,stretch_len=1)
point.color('white')
point.penup()
point.goto(0,0)
point.dx=10
point.dy=10




pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score : 0  High Score : 0",align="center",font=("courier",24,"normal"))
score=0
high=0
def snake_up():
    if snake.direction != "down":
        snake.direction = "up"

def snake_down():
    if snake.direction != "up":
        snake.direction = "down"

def snake_left():
    if snake.direction != "right":
        snake.direction = "left"

def snake_right():
    if snake.direction != "left":
        snake.direction = "right"

def move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)

    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)

    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)

    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)



wn.listen()
wn.onkeypress(snake_up, "Up")
wn.onkeypress(snake_down, "Down")
wn.onkeypress(snake_right, "Right")
wn.onkeypress(snake_left, "Left")
body=[]

while True:
    wn.update()
    move()
    time.sleep(speed)

    if snake.distance(point) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        point.goto(x, y)

        snake_body = turtle.Turtle()
        snake_body.speed(0)
        snake_body.shape('square')
        snake_body.color('white')
        snake_body.shapesize(stretch_wid=1, stretch_len=1)
        snake_body.penup()
        body.append(snake_body)
        score += 10

        speed-=0.001
        if score>high:
            high=score
        pen.clear()
        pen.write("Score : {}  High Score : {}".format(score, high), align="center", font=("courier", 24, "normal"))

    for i in range(len(body) - 1, 0, -1):
        x = body[i - 1].xcor()
        y = body[i - 1].ycor()
        body[i].goto(x, y)

    if (len(body) > 0):
        x = snake.xcor()
        y = snake.ycor()
        body[0].goto(x, y)

    if snake.xcor()>600 or snake.xcor()<-600 or snake.xcor()>600 or snake.xcor()<-600 :
        snake.goto(0,0)
        snake.direction="stop"


        for i in body:
            i.goto(1000,1000)
        body.clear()
       
        score=0
        pen.clear()
        pen.write("Score : {}  High Score : {}".format(score, high), align="center", font=("courier", 24, "normal"))








