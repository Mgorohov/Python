from functools import wraps
from time import perf_counter


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()

        try:
            return func(*args, **kwargs)
        finally:
            elapsed = perf_counter() - start
            print(f"{func.__name__}: {elapsed:.6f} сек")

    return wrapper


def validate_square(func):
    @wraps(func)
    def wrapper(matrix, *args, **kwargs):
        if not isinstance(matrix, list) or not matrix:
            raise ValueError("Ожидается квадратная матрица")

        for row in matrix:
            if not isinstance(row, list) or len(row) != len(matrix):
                raise ValueError("Матрица должна быть квадратной")

        return func(matrix, *args, **kwargs)

    return wrapper
