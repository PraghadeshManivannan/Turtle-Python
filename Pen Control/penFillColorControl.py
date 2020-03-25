# Pen control
# Drawing state 
import turtle

turtle = turtle.Turtle()

# turtle. penFillcolor(*args)
# return or set the penFillcolor

# penFillcolor()
# Return the current penFillcolor as color specification string or as a tuple

print(turtle.fillcolor())
turtle.fd(100)
turtle.lt(90)
turtle.fd(100)
turtle.lt(90)
turtle.fd(100)
turtle.lt(90)
turtle.fd(100)
turtle.pu()

# penFillcolor(colorstring)
# Set penFillcolor to colorstring, which is a Tk color specification string, such as "red","yellow", or "#33cc8c".

turtle.setx(200)
turtle.pd()
turtle.fillcolor("brown")
print(turtle.fillcolor())
turtle.fd(100)
turtle.lt(90)
turtle.fd(100)
turtle.lt(90)
turtle.fd(100)
turtle.lt(90)
turtle.fd(100)
turtle.pu()

# pencolor((r, g, b))
# Set penFillcolor to the RGB color represented by the tuple of r, g, and b. Each of r, gand b must be in the range 0..colormode, where colormode is either 1.0 or 255

turtle.setx(-100)
turtle.pd()
tup = (0.2, 0.8, 0.55)
turtle.fillcolor(tup)
print(turtle.fillcolor())
turtle.fd(100)
turtle.lt(90)
turtle.fd(100)
turtle.lt(90)
turtle.fd(100)
turtle.lt(90)
turtle.fd(100)
turtle.pu()

# pencolor(r, g, b)
# Set penFillcolor to the RGB color represented by r, g, and b. Each of r, gand b must be in the range 0..colormode.

turtle.sety(-150)
turtle.pd()
turtle.fillcolor('#32c18f')
print(turtle.fillcolor())
turtle.fd(100)
turtle.lt(90)
turtle.fd(100)
turtle.lt(90)
turtle.fd(100)
turtle.lt(90)
turtle.fd(100)

