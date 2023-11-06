import os


def checking_file(file):
    if os.path.exists(file):
        print('Файл {} существует'.format(file))


def error_log_generator(path):
    with open(path, 'r', encoding='utf8') as file:
        for elem in file.read().split('\n'):
            if not elem.find('ERROR'):
                yield elem


input_file_path = os.path.abspath(os.path.join('data', 'work_logs.txt'))
output_file_path = os.path.abspath(os.path.join('data', 'output.txt'))

checking_file(input_file_path)
checking_file(output_file_path)


with open(output_file_path, 'w', encoding='utf8') as output:
    for error_line in error_log_generator(input_file_path):
        print(error_line)
        output.write(error_line + '\n')
print("Файл успешно обработан.")
