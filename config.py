NAME = 'game of life'

# square sizes = 18 x 10
length = 18
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

# #### forms #### #

# 10 cell row
cell_row_10 = [
    [15, 21], [15, 22], [15, 23], [15, 24], [15, 25],
    [15, 26], [15, 27], [15, 28], [15, 29], [15, 30],
]

glider = [
    [14, 25], [15, 26], [16, 24], [16, 25], [16, 26]
]
