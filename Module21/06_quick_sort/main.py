def split_list(numbers):
    if len(numbers) <= 1:
        return numbers
    support = numbers[-1]
    left = []
    middle = []
    right = []
    for a in numbers:
        if a < support:
            left.append(a)
        elif a == support:
            middle.append(a)
        else:
            right.append(a)
    return split_list(left) + middle + split_list(right)

list_number = [5, 8, 9, 4, 2, 9, 1, 8]
print(split_list(list_number))
