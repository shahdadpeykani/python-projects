from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(500, 400)
guess = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter the color: ")
color = ["red", "blue", "orange", "purple", "green", "yellow"]
all_turtle = []
height = -100
for turtle in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color[turtle])
    all_turtle.append(new_turtle)
    new_turtle.penup()
    new_turtle.goto(-230, height)
    height += 30

if guess:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == guess:
                print(f"You've won. The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost. The {winning_color} turtle is the winner!")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
