import turtle
turtle = turtle.Turtle()

# turtle. reset()
# turtle. resetscreen()
# Reset all Turtles on the Screen to their initial state.
# Note: This TurtleScreen method is available as a global function only under the name resetscreen
# The global function reset is another one derived from the Turtle method 
# reset.

screen = turtle.getscreen()

screen.bgcolor("orange")
print(screen.bgcolor())
screen.delay(10)
turtle.reset()
print(screen.bgcolor())
screen.delay(10)


screen.bgcolor("#800080")
print(screen.bgcolor())
screen.delay(10)
turtle.reset()
print(screen.bgcolor())
screen.delay(10)
