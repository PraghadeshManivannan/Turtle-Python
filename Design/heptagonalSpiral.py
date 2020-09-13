from turtle import *
import random

#set the title
title('Heptagon Spiral')

#colors for the pentagon
color = ['red','yellow','blue','green','cyan','orange','pink']

#sets the screen color
bgcolor('black')

#hides the turtle
hideturtle()

#speed of the turtle
speed(0)

#pentagon spiral
for i in range(360):

  #color for the pentagon
  pencolor(color[i%7])

  #forwards the turtle
  forward((2*i)+1)

  #checks the width5
  width(i/100 + 1)

  #changes the angle of the pentagon
  left(54)
  
done()
