import turtle
turtle = turtle.Turtle()

# turtle. screensize(canvwidth=None, canvheight=None, bg=None)
# Parameters: canvwidth – positive integer, new width of canvas in pixels
# canvheight – positive integer, new height of canvas in pixels
# bg – colorstring or color-tuple, new background color
# If no arguments are given, return current (canvaswidth, canvasheight).
# Else resize the canvas the turtles are drawing on. Do not alter the drawing window. 
# To observe hidden parts of the canvas, use the scrollbars. 
# With this method, one can make visible those parts of a drawing which were outside the canvas before.

screen = turtle.getscreen()

print(screen.screensize())
screen.delay(10)

screen.screensize(2000,1500,'yellow')
print(screen.screensize())