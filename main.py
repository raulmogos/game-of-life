import pygame

from config import *
from helper import *


pygame.init()


screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(NAME)

# matrix in which we store each Rect object for displaying
matrix = []
# mat is for internal computation
mat = []

for i in range(no_squares['height']):
    _top = i * length + i * margin
    row, r = [], []
    for j in range(no_squares['width']):
        _left = j * length + j * margin
        rect = pygame.Rect(_left, _top, length, length)
        pygame.draw.rect(screen, GREEN, rect)
        row.append(rect)
        r.append(0)
    matrix.append(row)
    mat.append(r)


# current form that is iterating
form = glider
for cell in form:
    x, y = cell[0], cell[1]
    pygame.draw.rect(screen, BROWN, matrix[x][y])
    mat[x][y] = 1


run = True
pause = True

while run:

    pygame.time.delay(DELAY)

    for ev in pygame.event.get():
        if ev.type is pygame.QUIT:
            run = False
            break

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        pause = not pause
    if keys[pygame.K_UP]:
        mat = change_form(mat, cell_row_10)
        pause = True

    n, m = len(mat), len(mat[0])

    if not pause:
        # create the new matrix
        new_mat = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                alive = get_no_neighbours(i, j, mat)
                # rules
                # if is dead
                if mat[i][j] == 0:
                    if alive == 3:
                        # make it alive
                        new_mat[i][j] = 1
                    else:
                        new_mat[i][j] = 0
                # then it is alive aka matrix[i][j] == 1
                else:
                    if alive == 2 or alive == 3:
                        new_mat[i][j] = 1
                    else:
                        new_mat[i][j] = 0
        mat = new_mat

    for i in range(n):
        for j in range(m):
            if mat[i][j] == 0:
                pygame.draw.rect(screen, GREEN, matrix[i][j])
            else:
                pygame.draw.rect(screen, BROWN, matrix[i][j])
    pygame.display.update()


pygame.quit()
