from turtle import *
import random

#set the title
title('Square Spiral')

#colors for the square
color = ['red','green','blue','cyan']

#sets the screen color
bgcolor('black')

#hides the turtle
hideturtle()

#speed of the turtle
speed(0)

#square spiral
for i in range(360):

  #color for the square
  pencolor(color[i%4])

  #forwards the turtle
  forward((5*i)+1)

  #checks the width
  width(i/100 + 1)

  #changes the angle of the square
  left(92)
  
done()

