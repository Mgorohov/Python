from pathlib import Path

from .decorators import timer, validate_square
from .matrix_io import diagonal, flatten, matrices_generator, spiral
from .matrix_ops import (
    add,
    apply_to_matrix,
    determinant,
    get_stats,
    multiply,
    power,
    scalar_multiply,
    subtract,
    transpose,
    transpose_comprehension
)
from .matrix_utils import (
    matrix_stats,
    min_max_positions,
    print_matrix,
    read_matrix_from_console,
    read_matrix_from_file,
    write_matrix_to_file
)


DATA_DIR = Path(__file__).resolve().parent / "data"


@timer
@validate_square
def show_determinant(matrix):
    result = determinant(matrix)
    print("Определитель матрицы:", result)
    return result


@timer
@validate_square
def show_power(matrix, k, mod=None):
    if mod is None:
        result = power(matrix, k)
    else:
        result = power(matrix, k, mod=mod)

    print_matrix(result)
    return result


def get_current_matrix(matrix):
    if matrix is None:
        raise ValueError(
            "Сначала введите матрицу или загрузите её из файла"
        )

    return matrix


def additional_menu(matrix):
    print("\nДополнительные функции")
    print("1. Статистика матрицы")
    print("2. Применить функцию к элементам")
    print("3. Умножить матрицу на число")
    print("4. Сложить или вычесть матрицы")
    print("5. Вывести все элементы по порядку")
    print("6. Прочитать все матрицы из папки data")
    print("7. Показать число операций")

    choice = input("Выберите пункт: ")

    if choice == "1":
        print(matrix_stats(matrix))
        print(
            "Позиции (минимум, максимум):",
            min_max_positions(matrix)
        )

    elif choice == "2":
        print("1. Возвести все элементы в квадрат")
        print("2. Заменить отрицательные числа нулями")

        function_choice = input("Выберите функцию: ")

        if function_choice == "1":
            matrix = apply_to_matrix(
                matrix, lambda x: x ** 2
            )

        elif function_choice == "2":
            matrix = apply_to_matrix(
                matrix, lambda x: x if x > 0 else 0
            )

        else:
            print("Нет такого пункта")
            return matrix

        print_matrix(matrix)

    elif choice == "3":
        k = float(input("Введите число: "))
        matrix = scalar_multiply(matrix, k)
        print_matrix(matrix)

    elif choice == "4":
        operation = input("Введите + или -: ")

        if operation not in ("+", "-"):
            print("Неизвестная операция")
            return matrix

        print("Введите вторую матрицу:")
        second = read_matrix_from_console()

        if operation == "+":
            matrix = add(matrix, second)
        else:
            matrix = subtract(matrix, second)

        print_matrix(matrix)

    elif choice == "5":
        print(list(flatten(matrix)))

    elif choice == "6":
        for number, loaded_matrix in enumerate(
            matrices_generator(DATA_DIR), start=1
        ):
            print(f"Матрица {number}:")
            print_matrix(loaded_matrix)

    elif choice == "7":
        print(
            "Количество вызовов матричных операций:",
            get_stats()
        )

    else:
        print("Нет такого пункта")

    return matrix


def main():
    current = None
    original = None

    while True:
        print("\nМатричный калькулятор")
        print("1. Ввести матрицу с клавиатуры")
        print("2. Загрузить матрицу из файла")
        print("3. Транспонировать матрицу")
        print("4. Умножить две матрицы")
        print("5. Возвести матрицу в степень")
        print("6. Найти определитель")
        print("7. Вывести главную диагональ")
        print("8. Вывести матрицу по спирали")
        print("9. Сохранить матрицу в файл")
        print("10. Выход")
        print("11. Дополнительные функции")
        print("12. Вернуться к исходной матрице")

        try:
            choice = input("Введите пункт меню: ")

            if choice == "1":
                current = read_matrix_from_console()
                original = [row[:] for row in current]

                print_matrix(current)

            elif choice == "2":
                filename = input(
                    f"Имя файла [{DATA_DIR / 'input.txt'}]: "
                ).strip()

                if not filename:
                    filename = DATA_DIR / "input.txt"

                current = read_matrix_from_file(filename)
                original = [row[:] for row in current]

                print_matrix(current)

            elif choice == "3":
                matrix = get_current_matrix(current)

                print("1. Вложенные циклы")
                print("2. Списочное выражение")

                method = input("Выберите способ: ")

                first = transpose(matrix)
                second = transpose_comprehension(matrix)

                print(
                    "Результаты двух способов совпадают:",
                    first == second
                )

                if method == "1":
                    current = first

                elif method == "2":
                    current = second

                else:
                    raise ValueError("Выберите 1 или 2")

                print_matrix(current)

            elif choice == "4":
                matrix = get_current_matrix(current)

                print("Введите вторую матрицу:")
                second = read_matrix_from_console()

                current = multiply(matrix, second)
                print_matrix(current)

            elif choice == "5":
                matrix = get_current_matrix(current)

                k = int(input("Введите степень: "))
                mod_text = input(
                    "Введите mod или нажмите Enter: "
                ).strip()

                if mod_text:
                    current = show_power(
                        matrix, k, mod=int(mod_text)
                    )
                else:
                    current = show_power(matrix, k)

            elif choice == "6":
                show_determinant(
                    get_current_matrix(current)
                )

            elif choice == "7":
                print(
                    list(diagonal(
                        get_current_matrix(current)
                    ))
                )

            elif choice == "8":
                print(
                    list(spiral(
                        get_current_matrix(current)
                    ))
                )

            elif choice == "9":
                matrix = get_current_matrix(current)

                filename = input(
                    f"Имя файла [{DATA_DIR / 'output.txt'}]: "
                ).strip()

                if not filename:
                    filename = DATA_DIR / "output.txt"

                write_matrix_to_file(matrix, filename)
                print("Матрица сохранена")

            elif choice == "10":
                print("Работа завершена")
                break

            elif choice == "11":
                current = additional_menu(
                    get_current_matrix(current)
                )

            elif choice == "12":
                if original is None:
                    print(
                        "Сначала введите или загрузите матрицу"
                    )
                else:
                    current = [row[:] for row in original]

                    print("Исходная матрица восстановлена")
                    print_matrix(current)

            else:
                print("Нет такого пункта меню")

        except FileNotFoundError as error:
            print(
                f"Файл не найден: "
                f"{error.filename or 'проверьте путь'}"
            )

        except ValueError as error:
            print("Ошибка ввода:", error)

        except OSError as error:
            print("Ошибка работы с файлом:", error)

        except EOFError:
            print("\nВвод завершён. Программа закрывается.")
            break

        except KeyboardInterrupt:
            print("\nПрограмма остановлена пользователем.")
            break


if __name__ == "__main__":
    main()