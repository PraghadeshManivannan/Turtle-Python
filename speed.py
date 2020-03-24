import turtle

turtle = turtle.Turtle()

# turtle. speed(speed=None)
# speed – an integer in the range 0..10 or a speedstring
# If no argument is given, return current speed
# If input is a number greater than 10 or smaller than 0.5, speed is set to 0
''' fastest: 0
fast: 10
normal: 6
slow: 3
slowest: 1'''

# Attention: speed = 0 means that no animation takes place. forward/back makes turtle jump and likewise left/right make the turtle turn instantly.

print(turtle.speed())
turtle.fd(100)
turtle.rt(90)

turtle.speed('normal')
print(turtle.speed())
turtle.fd(100)
turtle.rt(90)


turtle.speed(1)
print(turtle.speed())
turtle.fd(100)
turtle.rt(90)
