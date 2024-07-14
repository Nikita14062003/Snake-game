from turtle import Turtle,Screen
import time
import random

s=Screen()
s.setup(width=800,height=600)
s.bgcolor("black")
s.title("Snake game")
s.tracer(0)

#food
f=Turtle()
f.shape("circle")
f.penup()
f.shapesize(stretch_len=0.75,stretch_wid=0.75)
f.color("blue")
rand_x=random.randint(-380,380)
rand_y=random.randint(-280,280)
f.goto(rand_x,rand_y)
def refresh():
    #for locating the food at different locations
    rand_x=random.randint(-380,380)
    rand_y=random.randint(-280,270)
    f.goto(rand_x,rand_y)    


def update_score(score):
    b.clear()
    b.write(f"Score:{score}",align="center",font=("Arial",24,"normal"))

b=Turtle()#for displaying score
score=0
b.color("white")
b.penup()
b.goto(0,260)
b.hideturtle()
update_score(score)

snake=[]
for i in range(3):#creating a snake
    t=Turtle()
    t.shape("square")
    t.color("white")
    t.penup()
    t.setposition(20*i,0)
    snake.append(t)

def add_segment(snake):
    #extending the length of snake
    n=Turtle()
    count=len(snake)
    n.shape("square")
    n.color("white")
    n.penup()
    x=snake[-1].xcor()
    y=snake[-1].ycor()
    n.setposition(x,y)
    snake.append(n)
    
def up():
    snake[0].setheading(90)
def down():
    snake[0].setheading(270)
def left():
    snake[0].setheading(180)
def right():
    snake[0].setheading(0)
s.listen()
s.onkey(up,"Up")
s.onkey(down,"Down")
s.onkey(left,"Left")
s.onkey(right,"Right")
game_on=True
while game_on:
    s.update()
    time.sleep(0.1)
    for i in range(len(snake)-1,0,-1):#for moving
        x=snake[i-1].xcor()
        y=snake[i-1].ycor()
        snake[i].goto(x,y)
    snake[0].forward(20)
    if snake[0].distance(f)< 18:#for detecting collision with food
        refresh()
        score+=1
        add_segment(snake)
        update_score(score)
    if snake[0].xcor()>390 or snake[0].xcor()<-390 or snake[0].ycor()>290 or snake[0].ycor()<-290:
        #for detecting collision with walls
        game_on=False
        b.goto(0,0)
        b.write("GAME OVER",align="center",font=("Arial",30,"bold"))
    for i in snake[3:]:#detecting collision with tail
        if snake[0].distance(i)<5:
            game_on=False
            b.goto(0,0)
            b.write("GAME OVER",align="center",font=("Arial",30,"bold"))            

s.exitonclick()
