from turtle import *
import random

#set the title
title('Rectangle Spiral')

#colors for the rectangle
color = ['red','green','blue','cyan']

#sets the screen color
bgcolor('black')

#hides the turtle
hideturtle()

#speed of the turtle
speed(0)

#rectangle spiral
for i in range(360):

  #color for the rectangle
  pencolor(color[i%4])

  if i%2 == 0:
    #forwards the turtle
    forward((3*i)+1)

  else: 
    #forwards the turtle
    forward((2*i)+0.5)

  #changes the angle of the rectangle
  left(92)
  
  #checks the width
  width(i/100 + 1)

done()


