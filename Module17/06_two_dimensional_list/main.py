def number(j):
    c = [n for n in range(j, 13, 4)]
    return c

list = [number(index) for index in range(1, 5)]
print(list)