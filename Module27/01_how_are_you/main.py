import functools
from typing import Callable, Any


def how_are_you(func: Callable) -> Callable:
    """
    Декоратор, который спрашивает КАК ДЕДА?
    Затем при любом ответе запускает дерируемую функцию.
    """
    @functools.wraps(func)
    def wrapper():
        input('Как дела? ')
        print('А у меня не очень! Ладно, держи свою функцию.')
        return print(func())

    return wrapper


@how_are_you
def test() -> str:
    """
    Функция, которая выводит на экран строку
    :return: строка
    """
    return '<Тут что-то происходит...>'


test()
print('\nФункция:\t{};\nДокументация:\t{}'.format(test.__name__, test.__doc__))
