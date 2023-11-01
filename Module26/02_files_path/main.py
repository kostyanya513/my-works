import os
from collections.abc import Iterable


def gen_find_dir(path: str) -> Iterable[str]:
    print('Текущая директория', path)
    for elem in os.walk(path):
        print('Директория', elem)
        for i_elem in elem:
            if isinstance(i_elem, list):
                for ind in i_elem:
                    r = os.path.join(path, ind)
                    yield r
            else:
                path = os.path.join(path, i_elem)


user_folder = 'Module25'
abs_path = os.path.abspath(os.path.join('..', '..', user_folder))
result = gen_find_dir(abs_path)

for i in result:
    print(i)
