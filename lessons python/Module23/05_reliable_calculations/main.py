import math


def get_sage_sqrt(num):
    try:
        if isinstance(num, int):
            return math.sqrt(num)
        elif isinstance(num, float):
            return math.sqrt(num)
        elif isinstance(num, str):
            raise SyntaxError
        elif num < 0:
            raise ValueError
    except ValueError as exc:
        return type(exc), 'Отрицательное число'
    except SyntaxError as exc:
        return type(exc), 'Строка'


numbers = [16, 25, -9, 0, 4.5, "abc"]
for number in numbers:
    result = get_sage_sqrt(number)
    print(f"Квадратный корень numbers {number}: {result}")
