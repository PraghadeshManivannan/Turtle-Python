import turtle
turtle = turtle.Turtle()

screen = turtle.getscreen()

# turtle. ontimer(fun, t=0)
# fun – a function with no arguments
# t – a number >= 0

running = True
def f():
    if running:
        turtle.fd(50)
        turtle.lt(60)
        screen.ontimer(f, 250)
f() ### makes the turtle march around
running = False