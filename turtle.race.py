import turtle
from turtle import Turtle
import random


# tim = Turtle()
# screen = turtle.Screen()
# def turtule_forword():
#     tim.forward(20)
# def turtul_back():
#     tim.backward(20)
# def left_tur():
#     # new_turn=tim.heading()+10
#     # tim.setheading(new_turn)
#     tim.left(45)
#     tim.forward(20)
# def right_tur():
#     # new_turn=tim.heading()-10
#     # tim.setheading(new_turn)
#     tim.right(45)
#     tim.forward(20)
# def clear():
#     tim.home()
#     tim.clear()
# screen.listen()
# print(tim.heading())
# screen.onkey(turtule_forword,"w" )
# screen.onkey(turtul_back,"s")
# screen.onkey(key="d",fun= right_tur)
# screen.onkey(key="a",fun= left_tur)
# screen.onkey(key="c",fun= clear)
# screen.exitonclick()
#11111111111111111111111111111111111111111111111111111111111111111111111
is_race_on = False
screen = turtle.Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

#Create 6 turtles
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        #230 is 250 - half the width of the turtle.
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        #Make each turtle move a random amount.
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()