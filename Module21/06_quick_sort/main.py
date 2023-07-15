# TODO здесь писать код
def split_three_list(structure, num,
                     struc=[], rezult_1=[], rezult_2=[], rezult_3=[]
                     ):
    for i in structure:
        if i < num:
            rezult_1.append(i)
        elif i == num:
            rezult_2.append(i)
        else:
            rezult_3.append(i)
    struc.append(rezult_1)
    struc.append(rezult_2)
    struc.append(rezult_3)
    print(struc)
    return struc


def sorting_list(numbers, v = [], t=None):
    number = numbers[-1]
    z = split_three_list(numbers, number)
    for i in z:
        n = i[-1]
        t = split_three_list(i, n)
        return t
    v.append(t)
    return v
#    print(t)
#    print(number)
#    print(split_three_list(numbers, number))


list_number = [5, 8, 9, 4, 2, 9, 1, 8]
print(sorting_list(list_number))
