import turtle

turtle1 = turtle.Turtle()

# turtle. distance(x, y=None)
# x – a number or a pair/vector of numbers or a turtle instance
# y – a number if x is a number, else None
# Return the distance from the turtle to (x,y), the given vector, or the given other turtle, in turtle step units.


#the distance to which the turtle has to be pointed
print(turtle1.distance(30,40))

#when the distance is given as tuple
print(turtle1.distance((30,40)))

joe = turtle.Turtle()

joe.fd(77)
print(turtle.distance(joe))


