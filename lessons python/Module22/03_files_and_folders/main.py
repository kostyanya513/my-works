import os


def counting_parametrs(user_path, count_files=0, file_size=0, subdirectory=0):
    for elem in os.listdir(user_path):
        i_path = os.path.join(user_path, elem)
        if os.path.isfile(i_path):
            file_size += os.path.getsize(i_path)
            count_files += 1
        elif os.path.isdir(i_path):
            subdirectory += 1
            count_files, file_size, subdirectory = counting_parametrs(i_path, count_files, file_size, subdirectory)
    return count_files, file_size, subdirectory


path = os.path.abspath(os.path.join('..', '..', 'Module22'))
result = counting_parametrs(path)

print('Количество файлов: %d' % result[0])
print('Размер каталога: %.2f Кб' % (result[1] / 1024))
print('Количество подкаталогов: %d' % result[2])
