import os
from collections.abc import Iterable


def gen_find_dir(file: str, path=os.path.abspath(os.path.sep)) -> Iterable[str]:
    print('Текущая директория', path)
    for adress, dirs, fils in os.walk(path):
        for name in fils:
            path_file = os.path.join(adress, name)
            if file in path_file.split('\\'):
                return
            else:
                yield path_file


user_folder = '03_str_count'
path_folder = 'F:\Desktop\Python_Basic'
result = gen_find_dir(user_folder, user_folder)

for i in result:
    print(i)
