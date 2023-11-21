from typing import Callable, Any
import functools
import datetime


def logging(func: Callable) -> Callable:
    """
    Декоратор, который логирует функции.
    При возникновении ошибки записывает ее в файл function_errors.log
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            print('Функция:\t{};\nДокументация:\t{}'.format(func.__name__, func.__doc__))
            return func(*args, **kwargs)
        except Exception as exp:
            exp = 'Exception: ошибка возникла - {}\n'.format(datetime.datetime.now())
            with open('function_errors.log', 'a', encoding='utf8') as file:
                file.write(exp)
                print(exp)

    return wrapper


@logging
def new_func() -> Any:
    """
    Функция, присваивает объекту значение 1
    :return: Any
    """
    x = 1
    return x


@logging
def next_func() -> Any:
    """
    Функция, присваивает объекту значение 1 / 0
    :return: Any
    """
    x = 1 / 0
    return x


@logging
def next_2_func() -> Any:
    """
    Функция, присваивает объекту значение 'Hello!'
    :return: Any
    """
    x = 'Hello!'
    return x


@logging
def next_3_func() -> Any:
    """
    Функция, присваивает объекту значение 'Hello!' / 5
    :return: Any
    """
    x = 6 / 5
    return x


new_func()
next_func()
next_2_func()
result = next_3_func()
print(result)
