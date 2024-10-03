import os
from typing import TextIO, Optional


class File:
    """
    Класс создает и открывает в режиме записи несуществующий файл.
    На выходе подавляются все исключения, связанные с файлами.
    Args:
        efile (str) имя файла
        file_mode (str) режим открытия файла
    """
    def __init__(self, efile: str, file_mode: str) -> None:
        self.efile = efile
        self.file_mode = file_mode
        self.i_file = None

    def __enter__(self) -> TextIO:
        if os.path.exists(self.efile):
            self.i_file = open(self.efile, self.file_mode, encoding='utf8')
        else:
            self.i_file = open(self.efile, 'w', encoding='utf8')
        return self.i_file

    def __exit__(self, exc_type, exc_val, exc_tb) -> Optional[bool]:
        self.i_file.close()
        if exc_type is IOError:
            return True


with File('example.txt', 'a') as file:
    file.write('Действие')
