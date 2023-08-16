name = input('Введите имя? ')
while True:
    print('Просмотр сообщения - 1, написать собщение - 2')
    action = int(input('Введите 1 или 2: '))
    if action == 1:
        try:
            with open('chat.txt', 'r', encoding='utf-8') as file:
                messeges = file.readline()
                print(''.join(messeges))
        except FileNotFoundError:
            print('Служебное сообщение: Пока ничего нет\n')
    elif action == 2:
        messege = input('Введите сообщение: ')
        with open('chat.txt', 'a', encoding='utf-8') as file:
            file.write('{}: {}\n'.format(name, messege))
    else:
        print('Неизвестная команда')