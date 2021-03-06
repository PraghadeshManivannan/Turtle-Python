import turtle

turtle = turtle.Turtle()

# turtle. shearfactor(shear=None)
# Parameters: shear – number (optional)
# Set or return the current shearfactor. 
# Shear the turtleshape according to the given shearfactor shear, which is the tangent of the shear angle. 
# Do not change the turtle’s heading (direction of movement). If shear is not given: return the current shearfactor
# i. e. the tangent of the shear angle, by which lines parallel to the heading of the turtle are sheared.

turtle.speed(1)
turtle.shape("circle")
turtle.shapesize(2,2)
turtle.fd(100)

turtle.shearfactor(0.5)
turtle.fd(100)
