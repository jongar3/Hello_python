import turtle
import pandas
import pathlib

FONT = ("Courier", 8, "normal")
PATH = pathlib.Path(__file__).resolve().parent
screen = turtle.Screen()
screen.title("US States Game")
image_path = PATH / "blank_states_img.gif"
screen.bgpic(str(image_path))

data= pandas.read_csv(PATH / "50_states.csv")
print(data)
states = list(data.state)
corrects=0
guessed_states=[]

while corrects <= len(states):
    # print(states)
    answer_state = turtle.textinput(f"{corrects}/{len(states)} corrects", prompt="Introduce a state").title()

    if answer_state in states:
        x_pos= data.x[data.state == answer_state]
        y_pos = data.y[data.state == answer_state]
        if answer_state not in guessed_states:
            pointer= turtle.Turtle()
            pointer.hideturtle()
            pointer.penup()
            pointer.goto(int(x_pos),int(y_pos))
            pointer.write(str(answer_state), align="center", font=FONT)
            corrects+=1
            guessed_states.append(answer_state)
        else:
            print("You already guessed this state")
    elif answer_state == "Exit":
        missing_states=[]
        for state in states:
            if state not in guessed_states:
                missing_states.append(state)
        missing_states_df = pandas.DataFrame(missing_states)
        missing_states_df.to_csv(PATH / "missing_states.csv")
        break

    else:
        print("Sorry, you didn't guess this state")



screen.mainloop()