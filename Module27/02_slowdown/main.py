import time
import functools
from typing import Callable


def delta_time(func: Callable) -> Callable:
    """ Декоратор, который перед выполнением функции ждет несколько секунд """

    @functools.wraps(func)
    def wrapper():
        time.sleep(3)
        return func()

    return wrapper


@delta_time
def calculate_cube() -> str:
    """
    Функция, которая выводит на экран текст
    :return: строка
    """
    return 'Hello!'


print('Результат:\t{}'.format(calculate_cube()))
print('\nФункция:\t{};\nДокументация:\t{}'.format(
    calculate_cube.__name__,
    calculate_cube.__doc__
))
