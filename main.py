import turtle
from os.path import dirname, join
import pandas as pd


current_dir = dirname(__file__)
csv_file = join(current_dir, "31_states.csv")
image_file = join(current_dir, "india_map.gif")

screen = turtle.Screen()
screen.setup(width=1000, height=1000)
screen.title("India States Game")

screen.addshape(image_file)
turtle.shape(image_file)

state_records = pd.read_csv(csv_file)
all_states = state_records["state"].to_list()

guessed_states = []

while len(guessed_states) < 31:
    
    answer_state = screen.textinput(title=f"{len(guessed_states)}/31 the state", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        remaining_states = [state for state in all_states if state not in guessed_states]
        data_df = pd.DataFrame(remaining_states)
        data_df.to_csv("states_to_learn.csv")
        break
    
# First of all we will check the answer state is one of the actual states list
    if answer_state not in guessed_states and answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()    
        state_data = state_records[state_records.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())
    else:
        print("Incorrect state guessed")
        print(f"{answer_state} is not in {all_states}")



# Code to get X & Y coordinates from the screen
# def get_mouse_click_coor(x, y):
#     print(x, y)
    
# turtle.onscreenclick(get_mouse_click_coor)

# Code to keep the screen the open
# turtle.mainloop() 
# or
# screen.exitonclick()