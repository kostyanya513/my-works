import os
from collections.abc import Iterable


def checking_file(file: str) -> None:
    if os.path.exists(file):
        print('Файл {} существует'.format(file))


def error_log_generator(path: str) -> Iterable[str]:
    with open(path, 'r', encoding='utf8') as file:
        for string in file.read().split('\n'):
            if not string.find('ERROR'):
                yield string


input_file_path = os.path.abspath(os.path.join('data', 'work_logs.txt'))
output_file_path = os.path.abspath(os.path.join('data', 'output.txt'))

checking_file(input_file_path)
checking_file(output_file_path)

with open(output_file_path, 'w', encoding='utf8') as output:
    for error_line in error_log_generator(input_file_path):
        print(error_line)
        output.write(error_line + '\n')
print("Файл успешно обработан.")
