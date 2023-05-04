n_man = 0
mans = int(input('Количество человек: '))
number = int(input('Какое число в считалке? '))
print('Значит выбывает каждый', number, end= '')
print('-й человек')
members = list(range(1, mans + 1))

while len(members) != 1:
    print('\nТекущий круг людей:', members)
    n_man = n_man + number - 1 - len(members)
    while n_man >= len(members):
        n_man -= len(members)
    print('Начало с номера', members[n_man])

    print('Выбывает человек под номером', members[n_man])
    members.remove(members[n_man])

print('\nОстался человек полд номером', members[n_man])