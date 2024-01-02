import time
from typing import Callable
import functools


class LoggerDecorator:
    def __init__(self, func: Callable) -> None:
        functools.update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs) -> None:
        print('Вызов функнции {}\nАргументы: {}'.format(self.func.__name__, args, kwargs))
        start = time.time()
        res = self.func(*args, **kwargs)
        end = time.time()
        execution_time = end - start
        print('Результат: {res}\nВремя выполнения: {time} секунд'.format(
            res=res,
            time=execution_time))


@LoggerDecorator
def complex_algorithm(arg1: int, arg2: int) -> int:
    # Здесь выполняется сложный алгоритм
    result = 0
    for i in range(arg1):
        for j in range(arg2):
            with open('test.txt', 'w', encoding='utf8') as file:
                file.write(str(i + j))
                result += i + j
    return result


# Пример вызова функции с применением декоратора
result = complex_algorithm(10, 50)
