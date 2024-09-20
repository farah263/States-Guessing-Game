from turtle import Turtle, Screen
import pandas

#Setting up the screen
screen = Screen()
screen.setup(730, 500)
screen.bgpic("blank_states_img.gif")

#Creating a turtle object
map_turtle = Turtle()
map_turtle.penup()
map_turtle.hideturtle()

data_df = pandas.read_csv("50_states.csv")                        
original_states = data_df["state"].tolist()   
x_coordinates = data_df["x"].tolist()
y_coordinates = data_df["y"].tolist()

guessed_state_list = []                                                                      
missed_state_list = []

user_input = screen.textinput("State_Name", "Please guess a state").title()      
while user_input != "Exit" or len(guessed_state_list) == 50:              
    if user_input in original_states and user_input not in guessed_state_list:        
        guessed_state_list.append(user_input)                                                
        index = original_states.index(user_input)                                           
        x_cord = x_coordinates[index]                                                        
        y_cord = y_coordinates[index]                                                       
        map_turtle.teleport(x_cord, y_cord)                                                  
        map_turtle.write(user_input)                                                         
    user_input = screen.textinput("State_Name", "Please guess a state").title()               

if len(guessed_state_list) < 51:                                                             
    missed_state_list = [m for m in original_states if m not in guessed_state_list]          
else:
    missed_state_list = "YOU GUESSED EVERYTHING PERFECTLY"  

user_guess_df = pandas.DataFrame(guessed_state_list, columns=["Guessed_States"])             
user_miss_df = pandas.DataFrame(missed_state_list, columns=["Missed_States"])

user_guess_df.to_csv('Guessed_States.csv', index=False)                                      
user_miss_df.to_csv('Missed_States.csv', index=False)
