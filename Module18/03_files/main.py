def check(symbols):
    for i_symbols in symbols:
        if text.startswith(i_symbols):
            return True

text = input('Название файла: ')
symbols = list('@№$%^&\*()')
if check(symbols):
    print('Ошибка: название начинается на один из специальных символов.')
elif not text.endswith('.txt') or text.endswith('.docs'):
    print('Неверное расширение!')
else:
    print('Файл назван верно!')
