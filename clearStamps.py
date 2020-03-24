import turtle

turtle = turtle.Turtle()

# turtle. clearstamps(n=None)
# n – an integer (or None)
#Delete all or first/last n of turtle’s stamps. 
# If n is None, delete all stamps
# If n > 0 delete first n stamps
# If n < 0 delete last n stamps.

turtle.setx(-200)
for i in range(8):
    turtle.stamp()
    turtle.fd(50)

turtle.clearstamps(2)
#deletes the first two stamps

turtle.clearstamps(-2)
#deletes the last two stamps


turtle.clearstamps()
#deletes the remaining stamps