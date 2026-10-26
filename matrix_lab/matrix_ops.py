OPS_COUNT = 0

def shape_matrix(matrix):
    if not matrix:
        raise ValueError("Пустая матрица")
    
    rows = len(matrix)
    cols = len(matrix[0])

    for row in matrix:
        if len(row) != cols:
            raise ValueError("Матрица не прмоугольная")
    
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

def multiply(a, b):
    global OPS_COUNT

    rows_a, cols_a = shape_matrix(a)
    rows_b, cols_b = shape_matrix(b)
    result = []

    if cols_a != rows_b:
        raise ValueError("Матрицы перемножтить невозможно")

    for i in range(rows_a):
        row = []

        for j in range(cols_b):
            sum = 0

            for h in range(cols_a):
                sum += a[i][h] * b[h][j]

            row.append(sum)

        result.append(row)

    OPS_COUNT += 1
    return result


    