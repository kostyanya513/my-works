first_line = input('Первая строка: ')
second_line = input('Вторая строка: ')
count = 0

while count != len(second_line):
    if second_line != first_line:
        d = second_line[-1:]
        c = second_line[:-1]
        second_line = second_line[-1:] + second_line[:-1]
        count += 1
    elif second_line == first_line:
        print('Первая строка получается из второй со сдвигом {}'.format(count))
        count = 0
        break

if count == len(second_line):
    print('Первую строку нельзя получить из второй с помощью циклического сдвига.')
