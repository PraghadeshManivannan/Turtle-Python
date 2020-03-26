import turtle
turtle = turtle.Turtle()

# turtle. clear()
# turtle. clearscreen()
# Delete all drawings and all turtles from the TurtleScreen. Reset the now empty
# TurtleScreen to its initial state: white background, no background image, no event bindings and tracing on.
# Note: This TurtleScreen method is available as a global function only under the name clearscreen.
#  The global function clear is a different one derived from the Turtle method clear.

screen = turtle.getscreen()

screen.bgcolor("orange")
print(screen.bgcolor())
screen.delay(10000)
screen.clear()
print(screen.bgcolor())
screen.delay(20000)

screen.bgcolor("#800080")
screen.delay(20000)
print(screen.bgcolor())
screen.clear()
print(screen.bgcolor())
