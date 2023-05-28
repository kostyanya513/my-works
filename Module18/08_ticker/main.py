def line(i):
    k = i_second.index(i)
    print(k)
    return k

first_line = input('Первая строка: ')
second_line = input('Вторая строка: ')
i_first = list(first_line)
i_second = list(second_line)
count = 0
for index in i_first:
    if index in i_second:
        number = line(index)
        break

new_first = [first_line[(first_line.index(variable) + number) % len(first_line)]
               for variable in second_line if variable in first_line]
if i_first == new_first:
    print('Первая строка получается из второй со сдвигом', number)
else:
    print('Первую строку нельзя получить из второй с помощью циклического сдвига.')
