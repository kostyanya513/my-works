def schet(list):
    for i_index in list:
        if i_index == 'h':
            break
    return list.index(i_index)

list = input('Введиет строку: ')
list_conversely = list[::-1]
print(list[len(list) - schet(list_conversely) - 2:schet(list):-1])
