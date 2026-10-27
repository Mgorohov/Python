import sys
from pathlib import Path


def print_matrix(matrix):
    if not matrix:
        raise ValueError("Пустая матрица")
    
    width = 0
    
    for row in matrix:
    
        for x in row:
            width = max(width, len(str(x)))
    
    for row in matrix:
        print(" ".join(f"{x:>{width}}" for x in row))


def write_matrix_to_file(matrix, filename):
    path = Path(filename)
    path.parent.mkdir(parents=True, exist_ok=True)

    if not matrix:
        raise ValueError("Пустая матрица")
    
    width = 0
    format_matrix = []
    
    for row in matrix:
    
        for x in row:
            width = max(width, len(str(x)))
    
    for row in matrix:
        format_matrix.append(" ".join(f"{x:>{width}}" for x in row))
    
    format_matrix = "\n".join(format_matrix)
    
    with open(path, "w", encoding="utf-8") as file:
        file.write(f"{len(matrix)} {len(matrix[0])}\n")
        file.write(format_matrix)
        file.write("\n")


def read_number(value):
    try:
        return int(value)
    except ValueError:
        return float(value)


def read_matrix(stream):
    line = stream.readline()

    if not line:
        raise ValueError("Не удалось прочитать размеры матрицы")

    sizes = line.split()

    if len(sizes) != 2:
        raise ValueError("Введите два размера матрицы: n m")

    n = int(sizes[0])
    m = int(sizes[1])

    if n <= 0 or m <= 0:
        raise ValueError("Размеры должны быть положительными")

    matrix = []

    for i in range(n):
        line = stream.readline()

        if not line:
            raise ValueError("Не хватает строк матрицы")

        numbers = line.split()

        if len(numbers) != m:
            raise ValueError(f"В строке должно быть {m} чисел")

        row = []

        for number in numbers:
            row.append(read_number(number))

        matrix.append(row)

    return matrix


def read_matrix_from_console():
    print("Введите размеры матрицы и затем её строки:")
    return read_matrix(sys.stdin)


def read_matrix_from_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return read_matrix(file)


def min_max_positions(matrix: list[list[int | float]]) -> tuple[tuple[int, int], tuple[int, int]]:
    if not matrix or not matrix[0]:
        raise ValueError("Матрица пустая")

    min_pos = (0, 0)
    max_pos = (0, 0)

    min_value = matrix[0][0]
    max_value = matrix[0][0]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            value = matrix[i][j]

            if value < min_value:
                min_value = value
                min_pos = (i, j)

            if value > max_value:
                max_value = value
                max_pos = (i, j)

    return min_pos, max_pos


def matrix_stats(matrix: list[list[int | float]]) -> dict[str, int | float]:
    numbers = []

    for row in matrix:
        for number in row:
            numbers.append(number)

    if not numbers:
        raise ValueError("Матрица пустая")

    counts = {}

    for number in numbers:
        counts[number] = counts.get(number, 0) + 1

    most_common = max(counts, key=counts.get)

    return {
        "min": min(numbers),
        "max": max(numbers),
        "sum": sum(numbers),
        "unique_count": len(set(numbers)),
        "most_common": most_common
    }

