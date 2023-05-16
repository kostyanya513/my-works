list = [(1 if i % 2 == 0 else i % 5) for i in range(int(input('Введите длину списка: ')))]
print('Результат:', list)