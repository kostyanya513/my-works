from collections.abc import Callable
import functools

user_permissions = ['admin']


def check_permission(access: str) -> Callable:
    """
    Декоратор проверяет, есть ли у пользователя доступ
    к вызываемой функции
    """

    def user_decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            if access in user_permissions:
                return func(*args, **kwargs)
            else:
                print('PermissionError: У пользователя недостаточно прав, чтобы выполнить функцию {}'.format(
                    func.__name__))

        return wrapped

    return user_decorator


@check_permission('admin')
def delete_site() -> None:
    print('Удаляем сайт')


@check_permission('user_1')
def add_comment() -> None:
    print('Добавляем комментарий')


delete_site()
add_comment()
