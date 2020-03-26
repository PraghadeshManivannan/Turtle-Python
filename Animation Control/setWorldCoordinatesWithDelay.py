import turtle
turtle = turtle.Turtle()

# turtle. setworldcoordinates(llx, lly, urx, ury)
# Parameters: llx – a number, x-coordinate of lower left corner of canvas
# lly – a number, y-coordinate of lower left corner of canvas
# urx – a number, x-coordinate of upper right corner of canvas
# ury – a number, y-coordinate of upper right corner of canvas
# Set up user-defined coordinate system and switch to mode “world” if necessary.
# This performs a screen.reset(). 
# If mode “world” is already active, all drawings are redrawn according to the new coordinates.
# ATTENTION: in user-defined coordinate systems angles may appear distorted.
screen = turtle.getscreen()
screen.reset()
screen.setworldcoordinates(-50,-7.5,50,7.5)
for _ in range(72):
    turtle.left(10)
screen.delay(5000)

for _ in range(8):
    turtle.left(45)
    turtle.fd(2)
