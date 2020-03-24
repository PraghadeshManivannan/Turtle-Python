import turtle

turtle = turtle.Turtle()

# turtle. clearstamp(stampid)
# stampid – an integer, must be return value of previous stamp() call
# Delete stamp with given stampid.

turtle.position()
#gives the position of the turtle

turtle.color("blue")

#storing the stamp id in stamp
stamp = turtle.stamp()

turtle.fd(50)
turtle.position()#gives the position of the turtle

turtle.clearstamp(stamp)# Delete stamp with given stampid.

turtle.position()#gives the position of the turtle
