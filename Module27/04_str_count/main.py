import functools
from typing import Callable


def counter(func: Callable) -> Callable:
    """
    Декоратор, который считывает и выводит количество вызовов
    декорируемой функции
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        return func(*args, **kwargs)
    wrapper.count = 0
    return wrapper


@counter
def dec_func() -> None:
    """
    Функция, которая ничего не выполняет
    """
    pass


enter_func = int(input('Сколько раз вызвать функцию? '))
for _ in range(enter_func):
    dec_func()
print('Функция {} вызвана {} раз.'.format(dec_func.__name__, dec_func.count))
print('Документация:\t{}'.format(dec_func.__doc__))
