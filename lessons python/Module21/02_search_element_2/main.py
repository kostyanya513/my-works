site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}


def search_key_site(structure, key, bool_depth, i_depth=0):
    if key in structure:
        return structure[key]
    if bool_depth == 'y':
        if i_depth > 0:
            for val_structure in structure.values():
                if isinstance(val_structure, dict):
                    i_value = search_key_site(val_structure, key, bool_depth, i_depth - 1)
                    if i_value:
                        break
            else:
                i_value = None
        else:
            i_value = None
    elif bool_depth == 'n':
        for val_structure in structure.values():
            if isinstance(val_structure, dict):
                i_value = search_key_site(val_structure, key, bool_depth, i_depth=0)
                if i_value:
                    break
        else:
            i_value = None
    return i_value


search_key = input('Введите искомый ключ: ')
depth = input('Хотите ввести максимальную глубину? Y/N: ').lower()
if depth == 'y':
    max_depth = int(input('Введите максимальную глубину: '))
elif depth == 'n':
    max_depth = 0
i_key = search_key_site(site, search_key, bool_depth=depth, i_depth=max_depth)
if i_key:
    print('Значение ключа:', i_key)
