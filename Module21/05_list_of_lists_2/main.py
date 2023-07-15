nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]

def expanded_list(structure, new_list = []):
    if isinstance(structure, (int, float, str)):
        new_list.append(structure)
    elif isinstance(structure, list):
        for element in structure:
            rezult = expanded_list(element)
    return new_list


print('Ответ: ', expanded_list(nice_list))
