import turtle
turtle = turtle.Turtle()

# turtle. bgpic(picname=None)
# picname – a string, name of a gif-file or "nopic", or None
# Set background image or return name of current backgroundimage.
# If picname is a filename, set the corresponding image as background.
# If picname is "nopic", delete background image, if present.
# If picname is None, return the filename of the current backgroundimage.

screen = turtle.getscreen()
print(screen.bgpic())

screen.bgpic("1.jpeg")
print(screen.bgpic())
