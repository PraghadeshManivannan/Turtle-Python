import turtle

turtle = turtle.Turtle()

# turtle. color(*args)
# Return or set pencolor and fillcolor.

turtle.pensize(5)
turtle.color("red", "yellow")
# turtle. filling()
# Return fillstate

# turtle. begin_fill()
# To be called just before drawing a shape to be filled.


turtle.begin_fill()
turtle.circle(80)

# turtle. end_fill()
# Fill the shape drawn after the last call to begin_fill().

turtle.end_fill()
