import turtle

turtle = turtle.Turtle()

# turtle. tilt(angle)
# Parameters: angle – a number
# Rotate the turtleshape by angle from its current tilt-angle, but do not change the turtle’s heading (direction of movement).

turtle.speed(1)
turtle.shape("circle")
turtle.shapesize(5,2)
turtle.tilt(30)
turtle.fd(50)
turtle.tilt(30)
turtle.fd(50)
