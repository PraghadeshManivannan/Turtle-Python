from turtle import *
import random

#set the title
title('Hexagonal Spiral')

#colors for the hexagon
color = ['red','yellow','orange','green','blue','cyan']

#sets the screen color
bgcolor('black')

#hides the turtle
hideturtle()

#speed of the turtle
speed(0)

#hexagonal spiral
for i in range(360):

  #color for the hexagon
  pencolor(color[i%6])

  #forwards the turtle
  forward(i)

  #checks the width
  width(i/100 + 1)

  #changes the angle of the hexagon
  left(57)
  
done()
