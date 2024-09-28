import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

guessed_states = []
while len(guessed_states) != 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 states correct",prompt="What's another state name").title()
    if answer_state == "Exit":
        missing_state = []
        for state in all_states:
            if state not in guessed_states:
                missing_state.append(state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("states_to_learn")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        tim = turtle.Turtle()
        tim.hideturtle()
        tim.penup()
        state_data = data[data.state == answer_state]
        tim.goto(int(state_data.x),int(state_data.y))
        # tim.write(answer_state)
        tim.write(state_data.state.item())
