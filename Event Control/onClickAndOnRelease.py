import turtle
turtle = turtle.Turtle()

# turtle. onclick(fun, btn=1, add=None)
# fun – a function with two arguments which will be called with the coordinates of the clicked point on the canvas
# num – number of the mouse-button, defaults to 1 (left mouse button) 
# add – True or False – if True, a new binding will be added, otherwise it will replace a former binding
# Bind fun to mouse-click events on this turtle. If fun is None, existing bindings are removed
def glow(x,y):
    turtle.fillcolor("red")
    
# turtle. onrelease(fun, btn=1, add=None)
# fun – a function with two arguments which will be called with the coordinates of the clicked point on the canvas
# num – number of the mouse-button, defaults to 1 (left mouse button)
# add – True or False – if True, a new binding will be added,otherwise it will replace a former binding
# Bind fun to mouse-button-release events on this turtle. If fun is None, existing bindings are removed.

def unglow(x,y):
    turtle.fillcolor("")
    
turtle.fd(100)
turtle.lt(90)
turtle.fd(100)
turtle.lt(90)
turtle.fd(100)
turtle.lt(90)
turtle.fd(100)
turtle.onclick(glow)
turtle.onrelease(unglow)
