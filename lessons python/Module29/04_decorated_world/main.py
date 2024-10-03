from collections.abc import Callable


def decorator_with_args_for_any_decorator(func: Callable) -> Callable:
    def wrapped(*args, **kwargs):
        print('Переданные арги и кварги в декоратор: {} {}'.format(args, kwargs))
        return func

    return wrapped


@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *args, **kwargs) -> Callable:
    def wrapped(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapped


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)


decorated_function("Юзер", 101)
