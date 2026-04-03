import turtle
import pandas
import tkinter.messagebox as messagebox

ALIGNMENT = ("center")
FONT = ("Arial", 14 , "bold")

screen = turtle.Screen()
screen.title("U.S States Game")
image = "Day-25 [int]/day-25-us-states-game-start/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("Day-25 [int]/day-25-us-states-game-start/50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(f"{len(guessed_states)}/50 States Correct", "What's another state's name?").title()

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("Day-25 [int]/day-25-us-states-game-start/states_to_learn.csv")

        messagebox.showinfo(
            title  = "Game Over",
            message = f"You guessed {len(guessed_states)}/50 states.\nCheck 'states_to_learn.csv to improve!\nClick anywhere on the window to exit."
        )
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        coor_data = data[data.state == answer_state]
        t.goto(coor_data.x.item(), coor_data.y.item())
        t.write(coor_data.state.item())

    if len(guessed_states) == 50:
        messagebox.showinfo(
            title = "🎉 Cngratulations 🎉",
            message = "You guessed all 50 states correctly!\nClick anywhere on the window to exit."
        )

screen.exitonclick()
