import turtle
turtle = turtle.Turtle()

screen = turtle.getscreen()

# turtle. textinput(title, prompt)
# Parameters: title – string
# prompt – string
# Pop up a dialog window for input of a string.
# Parameter title is the title of the dialog window, propmt is a text mostly describing what information to input.
# Return the string input. 
# If the dialog is canceled, return None.

name = screen.textinput('Name','Enter your name:')
print(name)