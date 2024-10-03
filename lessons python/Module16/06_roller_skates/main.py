list_shoes = []
list_legs = []
summ = 0
skates = int(input('Количество коньков: '))
for skate in range(skates):
    print('Размер', skate + 1, end='')
    print('-й пары:', end= ' ')
    shoe_size = int(input(''))
    list_shoes.append(shoe_size)

man = int(input('\nКоличество людей: '))
for leg in range(man):
    print('Размер ноги', leg + 1, end='')
    print('-го человека:', end= ' ')
    leg_size = int(input(''))
    list_legs.append(leg_size)

for man_shoes in list_legs:
    for ims in list_shoes:
        if ims == man_shoes:
            summ += 1
            list_shoes.remove(ims)
            break

print('\nНаибольшее количество людей, которые могут взять ролики:', summ)