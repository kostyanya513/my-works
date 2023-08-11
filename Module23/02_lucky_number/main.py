import random
summ = 0
with open('out_file.txt', 'w', encoding='utf-8') as numbers:
    try:
        while summ < 777:
            nums = int(input('Введите число: '))
            random_number = random.randint(1, 13)
            if random_number == 1:
                raise BaseException
            numbers.write(str(nums) + '\n')
            summ += nums
        print('Вы успешно выполнили условие для выхода из цикла!')
    except BaseException:
        print('Вас постигла неудача!')
