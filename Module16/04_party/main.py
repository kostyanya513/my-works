guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

# TODO здесь писать код

while True:
    print('Сейчас на вечеринке', len(guests), 'человек:', guests)
    d = input('Гость пришел или ушел? ')
    if d == 'пришел':
        man = input('Имя гостя: ')
        print('Привет,', guests)
        guests.append(man)
    elif d == 'ушел':
        man = input('Введите имя: ')
        print('Пока,', guests)
        guests.remove(man)
    elif d == 'пора спать':
        break
print('Вечеринка закончилась, все легли спать.')