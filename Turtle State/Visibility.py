import turtle

turtle = turtle.Turtle()

# turtle. hideturtle()
# turtle. ht()
# Make the turtle invisible. It’s a good idea to do this while you’re in the middle of doing
# some complex drawing, because hiding the turtle speeds up the drawing observably.
turtle.ht()
print(turtle.isvisible())
turtle.pensize(5)
turtle.color("red", "yellow")
turtle.begin_fill()
turtle.circle(80)
turtle.end_fill()

# turtle. showturtle()
# turtle. st()
# Make the turtle visible.
turtle.st()
print(turtle.isvisible())
