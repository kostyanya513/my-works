names = []
first_day = []
for i in range(8):
    name = input('Введите имя участника: ')
    names.append(name)

for index in range(8):
    if index % 2 == 0:
        first_day.append(names[index])

print('Первый день:', first_day)