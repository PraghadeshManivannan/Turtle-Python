import turtle

turtle = turtle.Turtle()

print(turtle.pos())
print(turtle.heading())

#drawing circle
#turtle.circle(radius,extent = None, steps = None)
#if radius is positive, the circle will be counter-clockwise or anti-clockwise
#if radius is negative,the cirlce will be drawn in clockwise direction
#extent gives the angle upto which the circle is to be drawn

#anit-clockwise circle

turtle.circle(50)
print(turtle.pos())
print(turtle.heading())


#clockwise circle

turtle.circle(-50,360,50)
print(turtle.pos())
print(turtle.heading())


