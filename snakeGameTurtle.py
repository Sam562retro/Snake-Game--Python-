from tkinter import CENTER
import turtle
import random
import time

score = 0
delay = 0.1
old_fruit = []

screen = turtle.Screen() #creating a screen 
screen.title("Snake Game")
screen.setup(width = 600, height = 600)
screen.tracer(20)
screen.bgcolor("black")

#creating a border
turtle.speed(5)
turtle.pensize(4)
turtle.pencolor("white")
turtle.penup()
turtle.goto(-250, 250)
turtle.pendown()
turtle.forward(500)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.forward(500)
turtle.hideturtle()

scoreTurtle = turtle.Turtle()
scoreTurtle.speed(5)
scoreTurtle.pencolor("white")
scoreTurtle.penup()
scoreTurtle.goto(0, 250)
scoreTurtle.write("score : 0", align = CENTER, font=("sans-serif", 30, "bold"))
scoreTurtle.hideturtle()

snake = turtle.Turtle() #making a snake object
snake.shape("square")
snake.pencolor("white")
snake.penup()
snake.goto(0,0)
snake.direction = "stop"

fruit = turtle.Turtle() #making a fruit object
fruit.speed(5)
fruit.penup()
fruit.shape("circle")
fruit.pencolor("red")
fruit.goto(random.randrange(-240, 240), random.randrange(-240, 240))

def snake_go_up():
    if snake.direction != "down":
        snake.direction = "up"

def snake_go_down():
    if snake.direction != "up":
        snake.direction = "down"

def snake_go_right():
    if snake.direction != "left":
        snake.direction = "right"

def snake_go_left():
    if snake.direction != "right":
        snake.direction = "left"

def move():
    if snake.direction == "up":
        snake.sety(snake.ycor() + 20)
    elif snake.direction == "down":
        snake.sety(snake.ycor() - 20)
    elif snake.direction == "right":
        snake.setx(snake.xcor() + 20)
    elif snake.direction == "left":
        snake.setx(snake.xcor() - 20)

def gameOver():
    screen.bgcolor("white")
    snake.direction = "stop"
    fruit.hideturtle()
    turtle.penup()
    turtle.goto(0,0)
    turtle.pencolor("red")
    turtle.write("GAME OVER", align = CENTER, font=("sans-serif", 60, "bold"))

screen.listen()
screen.onkeypress(snake_go_up, "Up")
screen.onkeypress(snake_go_down, "Down")
screen.onkeypress(snake_go_right, "Right")
screen.onkeypress(snake_go_left, "Left")
screen.onkeypress(snake_go_up, "w")
screen.onkeypress(snake_go_down, "s")
screen.onkeypress(snake_go_right, "d")
screen.onkeypress(snake_go_left, "a")

while True:
    screen.update()
    if snake.distance(fruit)<20:
        fruit.goto(random.randrange(-240, 240), random.randrange(-240, 240))
        score += 1
        delay -= 0.001
        scoreTurtle.clear()
        scoreTurtle.goto(0, 250)
        scoreTurtle.write("score : " + str(score), align = CENTER, font=("sans-serif", 30, "bold"))
        # making more turtles attach to the back of the snake
        newTurtle = turtle.Turtle()
        newTurtle.speed(5)
        newTurtle.penup()
        newTurtle.shape("square")
        newTurtle.pencolor("red")
        old_fruit.append(newTurtle)

    for i in range(len(old_fruit)-1, 0, -1):
        old_fruit[i].goto(old_fruit[i-1].xcor(), old_fruit[i-1].ycor())

    if len(old_fruit)>0:
        old_fruit[0].goto(snake.xcor(), snake.ycor())

    time.sleep(delay)
    move() 

    # -250, 250 (+500)
    if snake.xcor() > 250 or snake.xcor() < -250 or snake.ycor() > 250 or snake.ycor() < -250:
        gameOver()

    for i in range(len(old_fruit)-1, 0, -1):
        if old_fruit[i].distance(snake)<20:
            gameOver()
