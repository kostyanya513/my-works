guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:
    print('\nСейчас на вечеринке', len(guests), 'человек:', guests)
    d = input('Гость пришел или ушел? ')

    if d == 'пришел':
        man = input('Имя гостя: ')
        print('Привет,', man, '!')
        if len(guests) == 6:
            print('Прости', man, end= '')
            print(', но мест нет!')
        else:
            guests.append(man)
    elif d == 'ушел':
        man = input('Имя гостя: ')
        for dell_man in guests:
            if dell_man == man:
                print('Пока,', man, '!')
                guests.remove(man)
        print('Такого гостя нет!')
    elif d == 'пора спать':
        break
    else:
        print('Повторите команду!')

print('Вечеринка закончилась, все легли спать.')