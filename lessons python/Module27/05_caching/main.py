from typing import Callable
import functools


def decorator(func: Callable) -> Callable:
    """
    Декоратор, который выполняет задвнную функцию
    """

    @functools.wraps(func)
    def wrapper(num):
        value = func(num)
        return value

    return wrapper


def cache_args(func: Callable) -> Callable:
    """
    Декоратор, который создает словарь из аргументов и значений функции
    и при повторном вызове с теми же аргументами возвращает сохраненный резкльтат
    """
    dt = {}

    @functools.wraps(func)
    def wrapper(*args):
        if args not in dt:  # При каждом вызове проверяйте, не было ли уже аналогичного вызова
            dt[args] = func(*args)
        return dt[args]

    return wrapper


@cache_args
@decorator
def fibonacci(number: int) -> int:
    """
    Функция для вычисления чисел Фебоначчи
    :param number: int
    :return: int
    """
    if number <= 1:
        return number
    return fibonacci(number - 1) + fibonacci(number - 2)


# Вычисление числа Фибоначчи с использованием кеширования
print(fibonacci(10))  # Результат будет кеширован
#
# # Повторное вычисление числа Фибоначчи с теми же аргументами
print(fibonacci(10))  # Результат будет взят из кеша
#
# # Вычисление числа Фибоначчи с другим аргументом
print(fibonacci(5))  # Результат будет вычислен и закеширован
