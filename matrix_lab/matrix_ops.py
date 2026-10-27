OPS_COUNT = 0


def shape_matrix(matrix):
    if not matrix:
        raise ValueError("Пустая матрица")
    
    rows = len(matrix)
    cols = len(matrix[0])

    for row in matrix:
        if len(row) != cols:
            raise ValueError("Матрица не прямоугольная")
    
    return rows,cols


def transpose(matrix):
    global OPS_COUNT

    rows, cols = shape_matrix(matrix)
    result = []
    
    for j in range(cols):
        row = []
        
        for i in range(rows):
            row.append(matrix[i][j])

        result.append(row)

    OPS_COUNT += 1
    return result


def transpose_comprehension(matrix):
    global OPS_COUNT

    rows, cols = shape_matrix(matrix)

    result = [
        [matrix[i][j] for i in range(rows)]
        for j in range(cols)
    ]

    OPS_COUNT += 1
    return result


def multiply(a, b):
    global OPS_COUNT

    rows_a, cols_a = shape_matrix(a)
    rows_b, cols_b = shape_matrix(b)
    result = []

    if cols_a != rows_b:
        raise ValueError("Матрицы перемножить невозможно")

    for i in range(rows_a):
        row = []

        for j in range(cols_b):
            total = 0

            for h in range(cols_a):
                total += a[i][h] * b[h][j]

            row.append(total)

        result.append(row)

    OPS_COUNT += 1
    return result


def add(a, b):
    global OPS_COUNT

    if shape_matrix(a) != shape_matrix(b):
        raise ValueError("Матрицы разного размера нельзя сложить")

    result = []
    
    for i in range(len(a)):
        row = []

        for j in range(len(a[0])):
            row.append(a[i][j] + b[i][j])

        result.append(row)

    OPS_COUNT += 1
    return result


def subtract(a, b):
    global OPS_COUNT
    if shape_matrix(a) != shape_matrix(b):
        raise ValueError("Матрицы разного размера нельзя вычитать")

    result = []
    
    for i in range(len(a)):
        row = []

        for j in range(len(a[0])):
            row.append(a[i][j] - b[i][j])

        result.append(row)

    OPS_COUNT += 1
    return result


def scalar_multiply(matrix, k):
    global OPS_COUNT

    rows, cols = shape_matrix(matrix)
    result = []
    
    for i in range(rows):
        row = []

        for j in range(cols):
            row.append(matrix[i][j] * k)

        result.append(row)

    OPS_COUNT += 1
    return result


def determinant(matrix):
    global OPS_COUNT

    rows, cols = shape_matrix(matrix)
    if rows != cols:
        raise ValueError("Определитель считается только у квадратных матриц")

    if rows == 1:
        OPS_COUNT += 1
        return matrix[0][0]

    if rows == 2:
        OPS_COUNT += 1
        return((matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0]))

    result = 0

    for j in range(cols):
        minor = []

        for i in range(1, rows):
            row = []

            for h in range(cols):
                if h != j:
                    row.append(matrix[i][h])

            minor.append(row)

        result += (-1) ** j * matrix[0][j] * determinant(minor)

    OPS_COUNT += 1
    return result


def identity(n):
    global OPS_COUNT

    if n < 0:
        raise ValueError("Матрица не может быть отрицательного размера")

    result = []

    for i in range(n):
        row = []

        for j in range(n):
            if i == j:
                row.append(1)
            else:
                row.append(0)

        result.append(row)

    OPS_COUNT += 1
    return result


def power(matrix, k, *, mod=None):
    global OPS_COUNT

    rows, cols = shape_matrix(matrix)

    if rows != cols:
        raise ValueError("Матрица должна быть квадратной")
    if k < 0:
        raise ValueError("Степень не может быть отрицательной")
    if mod is not None and mod <= 0:
        raise ValueError("Мод должен быть положительным")

    def apply_mod(values):
        if mod is None:
            return [row[:] for row in values]

        result = []

        for row in values:
            new_row = []

            for elem in row:
                new_row.append(elem % mod)

            result.append(new_row)

        return result

    def fast_power(k):
        if k == 0:
            return apply_mod(identity(len(matrix)))

        if k == 1:
            return apply_mod(matrix)

        half = fast_power(k // 2)
        result = apply_mod(multiply(half, half))

        if k % 2 != 0:
            result = apply_mod(multiply(result, matrix))

        return result

    result = fast_power(k)
    OPS_COUNT += 1
    return result

def apply_to_matrix(matrix, func):
    global OPS_COUNT

    rows, cols = shape_matrix(matrix)
    result = []

    for i in range(rows):
        row = []

        for j in range(cols):
            row.append(func(matrix[i][j]))

        result.append(row)

    OPS_COUNT += 1
    return result


def get_stats():
    return OPS_COUNT
