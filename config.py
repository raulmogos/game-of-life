NAME = 'game of life'

# square sizes = 18 x 10
length = 16
no_squares = {
    'height': 30,
    'width': 50
}
square_width, square_height = length, length
margin = 1

# window set up
width = (no_squares['width'] * length) + (margin * no_squares['width'] - margin)
height = (no_squares['height'] * length) + (margin * no_squares['height'] - margin)
SIZE = width, height

# clock
DELAY = 100

# colors
GREEN = (22, 111, 77)
BROWN = (100, 77, 11)
RED = (153, 51, 0)
