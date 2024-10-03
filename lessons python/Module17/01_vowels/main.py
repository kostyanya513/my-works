def checking_list(i):
    new_list = [v_l for v_l in vowel_letters if v_l == i]
    return new_list

vowel_letters = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
list = list(input('Введите текст: '))
new = []
for i_list in list:
    new_list = checking_list(i_list)
    new.extend(new_list)

print('Список гласных букв:', new)
print('Длина списка:', len(new))