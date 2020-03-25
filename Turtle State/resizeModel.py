import turtle

turtle = turtle.Turtle()


turtle.pensize(10)
turtle.color('yellow','red')

# turtle. resizemode(rmode=None)
# rmode – one of the strings “auto”, “user”, “noresize”
# Set resizemode to one of the values: “auto”, “user”, “noresize”. 
# If rmode is not given,return current resizemode
# “auto”: adapts the appearance of the turtle corresponding to the value of pensize.
# “user”: adapts the appearance of the turtle according to the values of stretchfactor and outlinewidth (outline), which are set by shapesize().
# resizemode(“user”) is called by shapesize() when used with arguments.
# “noresize”: no adaption of the turtle’s appearance takes place
turtle.speed(1)
turtle.fd(100)
turtle.lt(90)

turtle.resizemode("auto")
turtle.fd(100)
turtle.lt(90)

turtle.resizemode("user")
turtle.shapesize(5, 5, 12)
turtle.fd(100)
turtle.lt(90)
