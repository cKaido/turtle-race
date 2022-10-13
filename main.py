from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
colors = ['red', 'orange', 'yellow', 'blue', 'green', 'purple']
user_bet = screen.textinput(title="Make your bet",
                            prompt="Which turtle will win the race? Enter a color: ")


for turtle_index in range(0, 6):
    tim = Turtle(shape='turtle')
    tim.penup()
    tim.goto(x=-230, y=-100)

screen.exitonclick()
