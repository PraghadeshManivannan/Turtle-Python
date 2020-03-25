# Pen control
# Drawing state 
import turtle

turtle = turtle.Turtle()

# Pull the pen down – drawing when moving.
# turtle. pendown()
# turtle. pd()
# turtle. down()
turtle.pd()
print(turtle.pos())

# Pull the pen up – no drawing when moving.
# turtle. penup() 
# turtle. pu() 
# turtle. up()
turtle.pu()
turtle.fd(100)
print(turtle.pos())
print(turtle.pensize())
# turtle. pensize(width=None)
# turtle. width(width=None)
# Parameters: width – a positive number
# Set the line thickness to width or return it. 
# If resizemode is set to “auto” and turtleshape is a polygon, that polygon is drawn with the same line thickness.
#  If no argument is given, the current pensize is returned.

turtle.pensize(20)
turtle.pd()
turtle.fd(100)
print(turtle.pensize())
