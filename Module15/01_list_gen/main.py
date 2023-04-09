numbers = []
number = int(input('Введите число: '))
for i in range(1, number + 1, 2):
    numbers.append(i)
print('Список из нечетных чисел от одного до N:', numbers)