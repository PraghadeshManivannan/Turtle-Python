import turtle

turtle = turtle.Turtle()

#placing the turtle at different position
print(turtle.pos())


#goto(x,y) or goto(x,y = None) 
#it will move the turtle to the respective position
#x and y will be float numbers 

turtle.goto(40.0,60.0)
print(turtle.pos())

#setpos(x,y) or setpos(x,y = None)
#it will move the turtle to the respective position
#x and y will be float numbers

turtle.setpos(60.0,40.0)
print(turtle.pos())

#setposition(x,y) or setposition(x,y = None)
#it will move the turtle to the respective position
#x and y will be float numbers

turtle.setposition(60.0,140.0)
print(turtle.pos())


#setx(x)
#x can be either float or integer

turtle.setx(140.0)
print(turtle.pos())

#sety(y)
#y can be either float or integer

turtle.sety(120.0)
print(turtle.pos())

#setheading(angle)
#angle can be either float or integer

turtle.setheading(90)
print(turtle.heading())


#seth(angle)
#angle can be either float or integer

turtle.seth(270)
print(turtle.heading())
