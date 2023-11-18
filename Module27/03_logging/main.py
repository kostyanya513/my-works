from typing import Callable
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
            func(*args, **kwargs)
        except Exception as exp:
            exp = 'Exception: ошибка возникла - {}\n'.format(datetime.datetime.now())
            with open('function_errors.log', 'a', encoding='utf8') as file:
                file.write(exp)
                print(exp)

    return wrapper


@logging
def new_func() -> None:
    """
    Функция, присваивает объекту значение 1
    :return: None
    """
    x = 1


@logging
def next_func() -> None:
    """
    Функция, присваивает объекту значение 1 / 0
    :return: None
    """
    x = 1 / 0


@logging
def next_2_func() -> None:
    """
    Функция, присваивает объекту значение 'Hello!'
    :return: None
    """
    x = 'Hello!'


@logging
def next_3_func() -> None:
    """
    Функция, присваивает объекту значение 'Hello!' / 5
    :return: None
    """
    x = 'Hello!' / 5


new_func()
next_func()
next_2_func()
next_3_func()
