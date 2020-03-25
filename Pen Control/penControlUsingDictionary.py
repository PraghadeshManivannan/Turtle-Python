# Pen control
# Drawing state 
import turtle

turtle = turtle.Turtle()

# turtle. pen(pen=None, **pendict)
# pen – a dictionary with some or all of the below listed keys
# pendict – one or more keyword-arguments with the below listed keys as keywords

# pen’s attributes in a “pen-dictionary” with the following key/value pairs:
# shown: True/False
# pendown: True/False
# pencolor: color-string or color-tuple
# fillcolor: color-string or color-tuple
# pensize: positive number
# speed: number in range 0..10
# resizemode: auto or user or noresize
# stretchfactor: (positive number, positive number)
# outline: positive number
# tilt: number

'''This dictionary can be used as argument for a subsequent call to pen() to restore the
former pen-state. Moreover one or more of these attributes can be provided as keywordarguments.
This can be used to set several pen attributes in one statement.'''

turtle.pen(fillcolor="yellow", pencolor="red", pensize=10)
turtle.fd(100)
turtle.lt(90)
turtle.fd(100)
turtle.lt(90)
turtle.fd(100)
turtle.lt(90)
turtle.fd(100)
