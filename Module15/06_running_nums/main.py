shift = int(input('Сдвиг: '))
list_elements = []
count = 1
number_elements = int(input('Количество элементов: '))

for index in range(number_elements):
    N = int(input('Число: '))
    list_elements.append(N)
print('Изначальный список:', list_elements)

for _ in range(shift):
    shifted_list = []
    new_element = list_elements[-1]
    shifted_list.append(new_element)
    for index in list_elements:
        count += 1
        shifted_list.append(index)
        if count == number_elements:
            break
    count = 1
    list_elements = shifted_list

print('Сдвинутый список:', shifted_list)