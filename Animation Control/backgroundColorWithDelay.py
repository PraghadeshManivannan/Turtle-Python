import turtle
turtle = turtle.Turtle()

# turtle. bgcolor(*args)
# args – a color string or three numbers in the range 0..colormode or a 3-tuple of such numbers
# Set or return background color of the TurtleScreen.

screen = turtle.getscreen()
screen.bgcolor("orange")
print(screen.bgcolor())
screen.delay(5000)

screen.bgcolor("#800080")
print(screen.bgcolor())
 

