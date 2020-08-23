
forms = [
    # 10 cell row
    [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ],
    # glider
    [
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 1],
    ],
    # small exploder
    [
        [0, 1, 0],
        [1, 1, 1],
        [1, 0, 1],
        [0, 1, 0],
    ],
    # exploder
    [
        [1, 0, 1, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 1, 0, 1],
    ],
    # tumbler
    [
        [0, 1, 1, 0, 1, 1, 0],
        [0, 1, 1, 0, 1, 1, 0],
        [0, 0, 1, 0, 1, 0, 0],
        [1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1],
        [1, 1, 0, 0, 0, 1, 1],
    ]
]


def get_from(nr):
    if nr >= len(forms):
        return forms[0], 1
    elif nr < 0:
        return forms[len(forms) - 1], 0
    else:
        return forms[nr], nr + 1


def compute_form_middle(mat, form):
    n, m = len(mat), len(mat[0])
    x, y = len(form), len(form[0])
    a, b = (n - x) // 2, (m - y) // 2
    new_mat = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(x):
        for j in range(y):
            new_mat[i + a][j + b] = form[i][j]
    return new_mat
