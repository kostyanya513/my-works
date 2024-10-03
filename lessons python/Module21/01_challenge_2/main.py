def sequence(number):
    print(number)
    if number == 1:
        return 1
    return sequence(number - 1)


num = int(input('Введите num: '))
sequence(num)
