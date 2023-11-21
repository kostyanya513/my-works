import time
import functools
from typing import Callable, Any


def delta_time(func: Callable) -> Callable:
    """ Декоратор, который перед выполнением функции ждет несколько секунд """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        time.sleep(3)
        return func(*args, **kwargs)

    return wrapper


@delta_time
def calculate_cube() -> Any:
    """
    Функция, которая выводит на экран текст
    :return: строка
    """
    print('Hello!')


calculate_cube()
print('\nФункция:\t{};\nДокументация:\t{}'.format(
    calculate_cube.__name__,
    calculate_cube.__doc__
))
