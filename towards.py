import turtle

turtle = turtle.Turtle()

# turtle. towards(x, y=None)
# x – a number or a pair/vector of numbers or a turtle instance
# y – a number if x is a number, else None
# Return the angle between the line from turtle position to position specified by (x,y),the vector or the other turtle
# This depends on the turtle’s start orientation which depends on the mode - “standard”/”world” or “logo”).

turtle.goto(10, 10)
print(turtle.towards(0,0))
