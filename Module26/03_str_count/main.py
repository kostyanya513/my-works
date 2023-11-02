import os
from collections.abc import Iterable


def counting_rows(strings: str) -> int:
    count = 0
    with open(strings, 'r', encoding='utf8') as file:
        for list_string in file.read().split('\n'):
            string = list_string.lstrip()
            if not string.startswith('#'):
                count += 1
    return count


def gen_find_dir(path: str) -> Iterable[str]:
    for elem in os.walk(path):
        for i_elem in elem:
            if isinstance(i_elem, list):
                for index in i_elem:
                    result = os.path.join(path, index)
                    if result.endswith('.py'):
                        y = f'Файл {result} имеет {counting_rows(result)} строк'
                        yield y
            else:
                path = os.path.join(path, i_elem)


user_folder = 'Module25'
abs_path = os.path.abspath(os.path.join('..', '..', user_folder))
desired_path = gen_find_dir(abs_path)

for i in desired_path:
    print(i)
