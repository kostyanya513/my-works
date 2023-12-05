import os
from typing import TextIO


class File:
    """
    Класс создает и открывает в режиме записи несуществующий файл.
    На выходе подавляются все исключения, связанные с файлами.
    """
    def __init__(self, efile) -> None:
        self.efile = efile
        self.i_file = None

    def __enter__(self) -> TextIO:
        if not os.path.exists(self.efile):
            self.i_file = open(self.efile, 'w', encoding='utf8')
            return self.i_file
        self.i_file = open(self.efile, 'w', encoding='utf8')
        print('Файл уже существует')
        return self.i_file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.i_file.close()
        if exc_type:
            return True


with File('example.txt') as file:
    file.write('Действие')
