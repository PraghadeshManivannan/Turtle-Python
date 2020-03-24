import turtle

turtle = turtle.Turtle()

print(turtle.pos())
print(turtle.heading())

#drawing circle
#turtle.circle(radius,extent = None, steps = None)
#if radius is positive, the circle will be counter-clockwise or anti-clockwise
#if radius is negative,the cirlce will be drawn in clockwise direction
#extent gives the angle upto which the circle is to be drawn


#semicircle
#anit-clockwise semi-circle

turtle.setx(140.0)
turtle.circle(50,180)
print(turtle.pos())
print(turtle.heading())


#clockwise semi-circle

turtle.circle(-50,180)
print(turtle.pos())
print(turtle.heading())

#quadrant circle
#anit-clockwise quadrant-circle

turtle.setx(-140.0)
turtle.circle(50,90)
print(turtle.pos())
print(turtle.heading())


#clockwise quadrant-circle

turtle.circle(-50,90)
print(turtle.pos())
print(turtle.heading())