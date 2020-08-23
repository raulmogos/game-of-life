
moves = [
    [1, 0], [0, 1], [-1, 0], [0, -1],
    [1, 1], [-1, -1], [-1, 1], [1, -1],
]


def get_no_neighbours(i, j, mat):
    alive = 0
    for move in moves:
        next_i = i + move[0]
        next_j = j + move[1]
        if next_i >= len(mat):
            next_i = 0
        elif next_i < 0:
            next_i = len(mat) - 1
        if next_j >= len(mat[0]):
            next_j = 0
        elif next_j < 0:
            next_j = len(mat[0]) - 1
        if mat[next_i][next_j] == 1:
            alive += 1
    return alive


def change_form(mat, new_form):
    n, m = len(mat), len(mat[0])
    mat = [[0 for _ in range(m)] for _ in range(n)]
    for cell in new_form:
        x, y = cell[0], cell[1]
        mat[x][y] = 1
    return mat
