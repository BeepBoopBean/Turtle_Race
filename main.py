from turtle import Turtle, Screen
import random


screen = Screen()

screen.setup(500, 400)

bet = screen.textinput('Bet on the turtle you think will win!', 'Pick: purple, orange, blue, red, pink, teal, or green')
print(f'You chose the {bet} turtle.')

colors = ['medium orchid', 'crimson', 'pink', 'deep sky blue', 'forest green', 'dark orange', 'medium blue']
color_names = ["purple", "red", "pink", "teal", "green", "orange", "blue"]
y_positions = [180, 120, 60, 0, -60, -120, -180]
all_turtles = []

for i in range(7):
    turt = Turtle('turtle')
    turt.color(colors[i])
    turt.up()
    turt.goto(-230, y_positions[i])
    all_turtles.append(turt)

is_race_on = True

while is_race_on:
    for x in all_turtles:
        if Turtle.xcor(x) >= 200:
            is_race_on = False
            winner = (all_turtles.index(x))
            print(f"The {color_names[winner]} turtle wins!")
            if bet == color_names[winner]:
                print("You win!")
            else:
                print("Better luck next time...")
        x.forward(random.randint(0, 10))


screen.exitonclick()
