import random

string = [random.randint(0, 100) for _ in range(10)]
print('Оригинальный описок:', string)
list_pair = []
for index in range(5):
    pair = (string[index * 2], string[index * 2 + 1])
    list_pair.append(pair)
print('Новый список:', list_pair)
