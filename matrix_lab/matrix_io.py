import os
from pathlib import Path
from .matrix_utils import read_matrix_from_file


def matrices_generator(folder):
    for filename in sorted(os.listdir(folder)):
        path = Path(folder) / filename

        if path.is_file() and path.suffix == ".txt":
            yield read_matrix_from_file(path)


def flatten(matrix):
    for row in matrix:
        for value in row:
            yield value


def diagonal(matrix):
    if not matrix:
        return

    for i in range(min(len(matrix), len(matrix[0]))):
        yield matrix[i][i]


def spiral(matrix):
    if not matrix:
        return

    top = 0
    bottom = len(matrix) - 1
    left = 0
    right = len(matrix[0]) - 1

    while top <= bottom and left <= right:
        for j in range(left, right + 1):
            yield matrix[top][j]

        top += 1

        for i in range(top, bottom + 1):
            yield matrix[i][right]

        right -= 1

        if top <= bottom:
            for j in range(right, left - 1, -1):
                yield matrix[bottom][j]

            bottom -= 1

        if left <= right:
            for i in range(bottom, top - 1, -1):
                yield matrix[i][left]

            left += 1
