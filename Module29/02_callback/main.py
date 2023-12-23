from typing import Callable, Dict

app: Dict[str, Callable] = {}


def callback(key: str) -> Callable:
    """
    Декоратор, добавляет в словарь функцию
    """
    def decorator_func(func: Callable) -> Callable:
        app[key] = func
        return func
    return decorator_func


@callback('//')
def example() -> str:
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


route = app.get('//')
print(route)
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')
print(app)
