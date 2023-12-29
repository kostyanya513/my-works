from datetime import datetime
import functools
import time
from collections.abc import Callable


def decorator(cls, format_str: str, func: Callable) -> Callable:
    """
    Декоратор, получает на вход класс, формат времени и даты, метод;
    выводит время запуска и сремя работы метода
    """
    @functools.wraps(cls)
    def wrapped_dec(*args, **kwargs):
        start = time.time()
        format_str_date = ''.join('%' + elem if elem.isalpha() else elem for elem in format_str)
        print("- Запускается '{}.{}'. Дата и время запуска: {}".format(
            cls.__name__,
            func.__name__,
            datetime.today().strftime(format_str_date)
        ))
        func(*args, **kwargs)
        end = time.time()
        print("- Завершение '{}.{}', время работы: {} s".format(
            cls.__name__,
            func.__name__,
            round(end - start, 3)
        ))
        return cls
    return wrapped_dec


def log_methods(format_str: str) -> Callable:
    """ Декоратор, получает на вход формат времени,
    декорирует методы класса"""
    def wrapped(cls):
        for i_metod in dir(cls):
            if not i_metod.startswith('__'):
                cur_metod = getattr(cls, i_metod)
                decoreted_metod = decorator(cls, format_str, cur_metod)
                setattr(cls, i_metod, decoreted_metod)
        return cls
    return wrapped


@log_methods("b d Y - H:M:S")
class A:
    def test_sum_1(self) -> int:
        print('Тут метод test_sum_1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])
        return result


@log_methods("b d Y - H:M:S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")

    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])
        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()
