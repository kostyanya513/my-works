def lenght(list, tuple):
    return min(len(list), len(tuple))


list = 'abfc'
tuple = (10, 20, 30, 40)
pair = ((list[index], tuple[index]) for index in range(lenght(list, tuple)))
print(pair)
pair_1 = [(list[index], tuple[index]) for index in range(lenght(list, tuple))]
print(pair_1)
print(zip(list, tuple))