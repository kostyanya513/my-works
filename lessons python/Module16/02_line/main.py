first_klass = []
second_klass = []
first_klass.extend(list(range(160, 177, 2)))
second_klass.extend(list(range(162, 181, 3)))
for second_index in second_klass:
    for first_index in first_klass:
        if second_index < first_index:
            count = first_klass.index(first_index)
            first_klass.insert(count, second_index)
            break
        elif second_index > first_klass[-1]:
            first_klass.append(second_index)
print('Отсортированный список учеников:', first_klass)