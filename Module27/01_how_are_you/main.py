import functools
from typing import Callable, Any


def how_are_you(func: Callable) -> Callable:
    """
    Декоратор, который спрашивает КАК ДЕДА?
    Затем при любом ответе запускает дерируемую функцию.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        input('Как дела? ')
        print('А у меня не очень! Ладно, держи свою функцию.')
        return func(*args, **kwargs)

    return wrapper


@how_are_you
def test(a: Any) -> Any:
    """
    Функция, которая выводит на экран строку
    :return: строка
    """
    print(a, 'Кукареку')


test(200)
print('\nФункция:\t{};\nДокументация:\t{}'.format(test.__name__, test.__doc__))
