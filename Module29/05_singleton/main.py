from typing import Callable
import functools


def singleton(cls) -> Callable:
    """
    Декоратор возвращает экземпляр класса
    """
    @functools.wraps(cls)
    def wrapped(*args, **kwargs):
        if not cls(*args, **kwargs):
            return cls

    return wrapped


@singleton
class Example:
    pass


my_obj = Example()
my_another_obj = Example()

print(id(my_obj))
print(id(my_another_obj))

print(my_obj is my_another_obj)
