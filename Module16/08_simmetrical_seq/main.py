def is_palindrom(sequence_list):
    new_list = []
    for i_num in range(len(sequence_list) - 1, -1, -1):
        new_list.append(sequence_list[i_num])
    if sequence_list == new_list:
        return True
    else:
        return False

sequence = []
new_sequence = []
chack = []
numbers = int(input('Количество чисел: '))
for index in range(numbers):
    number = int(input('Число: '))
    sequence.append(number)
print('Последовательность:', sequence)

for i_nums in range(0, numbers):
    for j_nums in range(i_nums, numbers):
        new_sequence.append(sequence[j_nums])
    if is_palindrom(new_sequence):
        for i_chack in range(0, i_nums):
            chack.append(sequence[i_chack])
        chack.reverse()
        break
    new_sequence = []

print('Нужно приписать чисел:', len(chack))
print('Сами числа:', chack)