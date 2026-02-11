import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_state = data.state.to_list()

guessed_states = []
score = 0

while len(guessed_states) < 50:
    answer_state = screen.textinput(f"{score}/50 Guess the state", "What is another state's name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in all_state if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_state:
        score += 1
        guessed_states.append(answer_state)
        timmy = turtle.Turtle()
        timmy.hideturtle()
        timmy.penup()
        state_data = data[data.state == answer_state]
        timmy.goto(state_data.x.item(), state_data.y.item())
        timmy.write(answer_state)
