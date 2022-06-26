import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S.States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
guessed_state =[]
not_guessed_state = []

# #to get the coordinate
# def get_mouse_click_coor(x,y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()


while len(guessed_state) < 50:
    guess_state = screen.textinput(title="Guess the state", prompt = "Enter the guessed state here").title()
    if guess_state == "Exit":
        break
   

    if guess_state in states: 
        guessed_state.append(guess_state)  
        s = turtle.Turtle()
        s.penup()
        s.hideturtle()
        state_data = data[data.state == guess_state]
        s.goto(int(state_data.x), int(state_data.y))
        s.write(state_data.state.item())
    for state in states:
        if state not in guessed_state:
            not_guessed_state.append(state)
            new_data = pandas.DataFrame(not_guessed_state)
            new_data.to_csv("new_data.csv")
            print(new_data)

