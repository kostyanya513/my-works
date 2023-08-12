def change_action(act):
    if act == '1':
        with open('chat_users.txt', 'r', encoding='utf-8') as messages_user:
            print(messages_user.read())
    elif act == '2':
        message = input('Введите сообщение: ')
        return chat.write(user + ': ' + message + '\n')


while True:
    chat = open('chat_users.txt', 'a', encoding='utf-8')
    user = input('Имя пользователя: ')
    action = input('Выберите одно из действий: 1. Посмотреть текст чата; 2. Отправить сообщение: ')
    change_action(action)
    chat.close()