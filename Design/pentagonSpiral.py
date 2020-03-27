from turtle import *
import random

#set the title
title('Pentagon Spiral')

#colors for the pentagon
color = ['red','yellow','green','blue','cyan']

#sets the screen color
bgcolor('black')

#hides the turtle
hideturtle()

#speed of the turtle
speed(0)

#pentagon spiral
for i in range(360):

  #color for the pentagon
  pencolor(color[i%5])

  #forwards the turtle
  forward((3*i)+1)

  #checks the width
  width(i/100 + 1)

  #changes the angle of the pentagon
  left(75)
  
done()
