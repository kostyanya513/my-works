glossary = {}
while True:
    action = input('Введите действие:'
                   '\n1. Добавить человека'
                   '\n2. Найти человека'
                   '\n')
    if action == '1':
        name = input('Введите имя и фамилию нового контакта (через пробел): ').split(' ')
        phon = int(input('Введите номер телефона: '))
        glossary[(name[0], name[1])] = phon
        print('Текущий словарь контактов:', glossary)
    elif action == '2':
        for man in glossary:
            search_name = input('Введите фамилию для поиска: ')
            if search_name in man:
                print(man[0], man[1], glossary[man])
    elif action == 'end':
        print('Работа завершена!')
        break
    else:
        print('Повторите ввод!')
