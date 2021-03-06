import turtle
turtle = turtle.Turtle()

# turtle. ondrag(fun, btn=1, add=None)
# fun – a function with two arguments which will be called with the coordinates of the clicked point on the canvas
# num – number of the mouse-button, defaults to 1 (left mouse button)
# add – True or False – if True, a new binding will be added,otherwise it will replace a former binding
# Bind fun to mouse-move events on this turtle. If fun is None, existing bindings are removed.
# Remark: Every sequence of mouse-move-events on a turtle is preceded by a mouse-click event on that turtle.
# Subsequently, clicking and dragging the Turtle will move it across the screen thereby producing handdrawings (if pen is down).

turtle.ondrag(turtle.goto)