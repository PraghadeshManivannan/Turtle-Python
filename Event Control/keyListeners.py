# turtle. listen(xdummy=None, ydummy=None)
# Set focus on TurtleScreen (in order to collect key-events). 
# Dummy arguments are provided in order to be able to pass listen() to the onclick method.
# turtle. onkey(fun, key)
# turtle. onkeyrelease(fun, key)
# Parameters: fun – a function with no arguments or None
# key – a string: key (e.g. “a”) or key-symbol (e.g. “space”)
# Bind fun to key-release event of key. If fun is None, event bindings are removed. 
# Remark: in order to be able to register key-events, TurtleScreen must have the focus

import turtle
turtle = turtle.Turtle()

screen = turtle.getscreen()
def f():
    turtle.fd(50)
    turtle.lt(90)
def g():
    turtle.rt(90)
    turtle.bk(50)

screen.onkeypress(f, "Up")
screen.onkeyrelease(g,"Up")
screen.listen()

# turtle. onkeypress(fun, key=None)
# Parameters: fun – a function with no arguments or None
# key – a string: key (e.g. “a”) or key-symbol (e.g. “space”)
# Bind fun to key-press event of key if key is given, or to any key-press-event if no key is
# given. Remark: in order to be able to register key-events, TurtleScreen must have focus.
# (See method listen().)
