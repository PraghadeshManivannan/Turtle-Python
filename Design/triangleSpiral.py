from turtle import *
import random

#set the title
title('Triangle Spiral')

#colors for the triangle
color = ['red','green','cyan']

#sets the screen color
bgcolor('black')

#hides the turtle
hideturtle()

#speed of the turtle
speed(10)

#triangle spiral
for i in range(360):

  #color for the square
  pencolor(color[i%3])

  #forwards the turtle
  forward((5*i)+1)

  #checks the width
  width(i/100 + 1)

  #changes the angle of the triangle
  left(122)
  
done()

