# Pen control
# Drawing state 
import turtle

turtle = turtle.Turtle()

# turtle. pencolor(*args)
# return or set the pencolor

# pencolor()
# Return the current pencolor as color specification string or as a tuple

print(turtle.pencolor())
turtle.fd(100)
turtle.lt(90)

# pencolor(colorstring)
# Set pencolor to colorstring, which is a Tk color specification string, such as "red","yellow", or "#33cc8c".

turtle.pencolor("brown")
print(turtle.pencolor())
turtle.fd(100)
turtle.lt(90)

# pencolor((r, g, b))
# Set pencolor to the RGB color represented by the tuple of r, g, and b. Each of r, gand b must be in the range 0..colormode, where colormode is either 1.0 or 255

tup = (0.2, 0.8, 0.55)
turtle.pencolor(tup)
print(turtle.pencolor())
turtle.fd(100)
turtle.lt(90)

# pencolor(r, g, b)
# Set pencolor to the RGB color represented by r, g, and b. Each of r, gand b must be in the range 0..colormode.

turtle.pencolor('#32c18f')
print(turtle.pencolor())
turtle.fd(100)
turtle.lt(90)

